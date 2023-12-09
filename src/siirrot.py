from math import inf
#from random import randint
from ruudukko import Ruudukko

class Peli:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False
        self.mahdolliset_siirrot = []
        self.siirrot = 0

    def tarkista_siirto(self, rivi, sarake):
        self.virhe = False
        if not rivi.isnumeric() or not sarake.isnumeric():
            self.virhe = True
            print("Väärä koordinaatti")
        elif int(rivi) not in range(1, 21) or int(sarake) not in range(1, 21):
            self.virhe = True
            print("Väärä koordinaatti")
        return self.virhe

    def tee_siirto(self, siirto, pelaaja):
        self.pelilauta.ruudukko[siirto[0]][siirto[1]] = pelaaja

    def pelaa(self):
        voittaja = None
        while True:
            self.pelilauta.tulosta_ruudukko()

            while True:
                rivi = input(("Valitse rivi 1-20: "))
                sarake = input("Valitse sarake 1-20: ")
                if not self.tarkista_siirto(rivi, sarake):
                    break
            siirto = (int(rivi) - 1, int(sarake) - 1)
            if self.pelilauta.ruudukko[siirto[0]][siirto[1]] == "-":
                self.tee_siirto(siirto, "X")
                self.etsi_mahdolliset_siirrot(siirto)
                self.siirrot += 1
                if self.etsi_voittajaa(siirto, "X"):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = "X"
                    break

            ai_siirto = self.etsi_paras_siirto(siirto, self.mahdolliset_siirrot)
            self.etsi_mahdolliset_siirrot(ai_siirto)
            print("Tietokoneen vuoro")
            if self.pelilauta.ruudukko[ai_siirto[0]][ai_siirto[1]] == "-":
                self.tee_siirto(ai_siirto, "O")
                self.siirrot += 1
                if self.etsi_tasapeli(self.siirrot):
                    break
                if self.etsi_voittajaa(ai_siirto, "O"):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = "O"
                    break
        if voittaja is not None:
            print(f"Voittaja on {voittaja}")
        else:
            print("Tasapeli")

    def etsi_voittajaa(self, siirto, pelaaja):
        rivi = siirto[0]
        sarake = siirto[1]
        laskuri = 0
        ruudut = self.pelilauta.ruudukko
        for i in range(rivi - 1, max(-1, rivi - 5), -1):
            if ruudut[i][sarake] == pelaaja:
                laskuri += 1
            else:
                break
        for i in range(rivi + 1, min(20, rivi + 5)):
            if ruudut[i][sarake] == pelaaja:
                laskuri += 1
            else:
                break
        if laskuri + 1 >= 5:
            return True
        laskuri = 0
        for j in range(sarake - 1, max(-1, sarake - 5), -1):
            if ruudut[rivi][j] == pelaaja:
                laskuri += 1
            else:
                break
        for j in range(sarake + 1, min(20, sarake + 5)):
            if ruudut[rivi][j] == pelaaja:
                laskuri += 1
            else:
                break
        if laskuri + 1 >= 5:
            return True
        laskuri = 0
        for k in range(1, 5):
            i = rivi - k
            j = sarake - k
            if i < 0 or j < 0:
                break
            if ruudut[i][j] == pelaaja:
                laskuri += 1
            else:
                break
        for k in range(1, 5):
            i = rivi + k
            j = sarake + k
            if i > 19 or j > 19:
                break
            if ruudut[i][j] == pelaaja:
                laskuri += 1
            else:
                break
        if laskuri + 1 >= 5:
            return True
        laskuri = 0
        for k in range(1, 5):
            i = rivi - k
            j = sarake + k
            if i < 0 or j > 19:
                break
            if ruudut[i][j] == pelaaja:
                laskuri += 1
            else:
                break
        for k in range(1, 5):
            i = rivi + k
            j = sarake - k
            if i > 19 or j < 0:
                break
            if ruudut[i][j] == pelaaja:
                laskuri += 1
            else:
                break
        if laskuri + 1 >= 5:
            return True
        return False

    def etsi_mahdolliset_siirrot(self, siirto):
        rivi = siirto[0]
        sarake = siirto[1]
        if (rivi, sarake) in self.mahdolliset_siirrot:
            self.mahdolliset_siirrot.remove((rivi, sarake))
        ruudut = self.pelilauta.ruudukko
        for i in range(rivi - 1, max(-1, rivi - 3), -1):
            if ruudut[i][sarake] == "-" and (i, sarake) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, sarake))

        for i in range(rivi + 1, min(20, rivi + 3)):
            if ruudut[i][sarake] == "-" and (i, sarake) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, sarake))

        for j in range(sarake - 1, max(-1, sarake - 3), -1):
            if ruudut[rivi][j] == "-" and (rivi, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((rivi, j))

        for j in range(sarake + 1, min(20, sarake + 3)):
            if ruudut[rivi][j] == "-" and (rivi, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((rivi, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake - k
            if i < 0 or j < 0:
                break
            if ruudut[i][j] == "-" and (i, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake + k
            if i > 19 or j > 19:
                break
            if ruudut[i][j] == "-" and (i, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake + k
            if i < 0 or j > 19:
                break
            if ruudut[i][j] == "-" and (i, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake - k
            if i > 19 or j < 0:
                break
            if ruudut[i][j] == "-" and (i, j) not in self.mahdolliset_siirrot:
                self.mahdolliset_siirrot.append((i, j))

    def etsi_tasapeli(self, siirtomaara):
        if siirtomaara == 400:
            return True
        
    def arvioi_siirto(self, siirto, pelaaja):
        siirron_arvo = -inf
        ruudut = self.pelilauta.ruudukko
        


    def minmax(self, pelilauta, siirto, mahdolliset_siirrot, syvyys, maksimoi):
        # arvot = {"X": 1, "O": -1}

        if self.etsi_voittajaa(siirto, "X"):
            return -inf
        if self.etsi_voittajaa(siirto, "O"):
            return inf
        if syvyys == 0:
            return 0
        if self.etsi_tasapeli(self.siirrot):
            return 0

        if maksimoi:
            max_arvo = -inf
            siirtolistan_kopio = self.mahdolliset_siirrot
            for siirto_tuple in mahdolliset_siirrot:
                pelilauta[siirto_tuple[0]][siirto_tuple[1]] = "O"
                siirtolistan_kopio.append(siirto_tuple)
                arvo = self.minmax(pelilauta, siirto_tuple, siirtolistan_kopio, syvyys + 1, False)
                pelilauta[siirto_tuple[0]][siirto_tuple[1]] = "-"
                max_arvo = max(max_arvo, arvo)
            return max_arvo

        else:
            min_arvo = inf
            siirtolistan_kopio = self.mahdolliset_siirrot
            for siirto_tuple in mahdolliset_siirrot:
                pelilauta[siirto_tuple[0]][siirto_tuple[1]] = "X"
                siirtolistan_kopio.append(siirto_tuple)
                arvo = self.minmax(pelilauta, siirto_tuple, siirtolistan_kopio, syvyys + 1, True)
                pelilauta[siirto_tuple[0]][siirto_tuple[1]] = "-"
                min_arvo = min(min_arvo, arvo)
            return min_arvo

    def etsi_paras_siirto(self, edellinen_siirto, mahdolliset_siirrot):
        paras_arvo = -inf
        paras_siirto = None

        for siirto in mahdolliset_siirrot:
            self.pelilauta.ruudukko[siirto[0]][siirto[1]] = "O"
            siirron_arvo = \
                self.minmax(self.pelilauta.ruudukko, edellinen_siirto, mahdolliset_siirrot, 0, False)
            self.pelilauta.ruudukko[siirto[0]][siirto[1]] = "-"

            if siirron_arvo > paras_arvo:
                paras_siirto = siirto
                paras_arvo = siirron_arvo

        return paras_siirto
