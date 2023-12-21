from math import inf
from random import choice
from ruudukko import Ruudukko

PLAYER = "X"
COMPUTER = "O"
EMPTY = "-"

class Peli:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False
        self.mahdolliset_siirrot = set()
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
                self.tee_siirto(siirto, PLAYER)
                self.etsi_mahdolliset_siirrot(siirto, self.mahdolliset_siirrot)
                #print(self.mahdolliset_siirrot)
                self.siirrot += 1
                if self.etsi_voittajaa(siirto, PLAYER, self.pelilauta):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = "X"
                    break

            ai_siirto = self.etsi_paras_siirto(self.mahdolliset_siirrot, self.pelilauta)
            self.etsi_mahdolliset_siirrot(ai_siirto, self.mahdolliset_siirrot)
            #print(self.mahdolliset_siirrot)
            print("Tietokoneen vuoro")
            if self.pelilauta.ruudukko[ai_siirto[0]][ai_siirto[1]] == "-":
                self.tee_siirto(ai_siirto, COMPUTER)
                self.siirrot += 1
                if self.etsi_tasapeli(self.siirrot):
                    break
                if self.etsi_voittajaa(ai_siirto, COMPUTER, self.pelilauta):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = "O"
                    break
        if voittaja is not None:
            print(f"Voittaja on {voittaja}")
        else:
            print("Tasapeli")

    def etsi_voittajaa(self, siirto, pelaaja, pelilauta):
        rivi = siirto[0]
        sarake = siirto[1]
        laskuri = 0
        try:
            ruudut = pelilauta.ruudukko
        except:
            ruudut = pelilauta
        if ruudut[rivi][sarake] == pelaaja:
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

    def etsi_mahdolliset_siirrot(self, siirto, mahdolliset_siirrot):
        rivi = siirto[0]
        sarake = siirto[1]
        ruudut = self.pelilauta.ruudukko
        if siirto in mahdolliset_siirrot:
            mahdolliset_siirrot.remove(siirto)
        for i in range(rivi - 1, max(-1, rivi - 3), -1):
            if ruudut[i][sarake] == "-":
                mahdolliset_siirrot.add((i, sarake))

        for i in range(rivi + 1, min(20, rivi + 3)):
            if ruudut[i][sarake] == "-":
                mahdolliset_siirrot.add((i, sarake))

        for j in range(sarake - 1, max(-1, sarake - 3), -1):
            if ruudut[rivi][j] == "-":
                mahdolliset_siirrot.add((rivi, j))

        for j in range(sarake + 1, min(20, sarake + 3)):
            if ruudut[rivi][j] == "-":
                mahdolliset_siirrot.add((rivi, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake - k
            if i < 0 or j < 0:
                break
            if ruudut[i][j] == "-":
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake + k
            if i > 19 or j > 19:
                break
            if ruudut[i][j] == "-":
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake + k
            if i < 0 or j > 19:
                break
            if ruudut[i][j] == "-":
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake - k
            if i > 19 or j < 0:
                break
            if ruudut[i][j] == "-":
                mahdolliset_siirrot.add((i, j))

    def etsi_tasapeli(self, siirtomaara):
        if siirtomaara == 400:
            return True
        
    def arvioi_pelitilanne(self, pelilauta, siirto):
        tilanteen_arvo = 0
        pelaaja = COMPUTER
        vastustaja = PLAYER
        rivi = siirto[0]
        sarake = siirto[1]
        try:
            ruudut = pelilauta.ruudukko
        except:
            ruudut = pelilauta
        try:
            ruudut_ennen_siirtoa = pelilauta.ruudukko.copy()
        except:
            ruudut_ennen_siirtoa = pelilauta.copy()
        ruudut_ennen_siirtoa[rivi][sarake] = "-"
        merkit = ""
        merkit2 = ""

        for j in range(max(0, sarake - 4), min(20, sarake + 5)):
            merkit += ruudut[rivi][j]
            merkit2 += ruudut_ennen_siirtoa[rivi][j]
        #if vastustaja in merkit:
            #print(f"vaaka: {merkit}")
        if EMPTY + pelaaja * 4 + EMPTY in merkit and EMPTY + pelaaja * 4 +EMPTY not in merkit2:
            tilanteen_arvo += 200
        if (EMPTY + pelaaja * 4 in merkit and EMPTY + pelaaja * 4 not in merkit2) or (pelaaja * 4 + EMPTY in merkit and pelaaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo += 150
        if EMPTY + pelaaja * 3 + EMPTY in merkit and EMPTY + pelaaja * 3 + EMPTY not in merkit2:
            tilanteen_arvo += 100
        if (EMPTY + pelaaja * 3 in merkit and EMPTY + pelaaja * 3 not in merkit2) or (pelaaja * 3 + EMPTY in merkit and pelaaja * 3 + EMPTY not in merkit2):
            tilanteen_arvo += 70
        if EMPTY + vastustaja * 4 + EMPTY in merkit and EMPTY + vastustaja * 4 + EMPTY not in merkit2:
            tilanteen_arvo -= 200
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 150
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 70
        if EMPTY + vastustaja * 3 + EMPTY in merkit:
            tilanteen_arvo -= 100
        #if vastustaja in merkit and siirto:
            #print(merkit)
            #print(siirto, tilanteen_arvo)
        merkit = ""
        merkit2 = ""

        for i in range(max(0, rivi - 4), min(20, rivi + 5)):
            merkit += ruudut[i][sarake]
            merkit2 += ruudut[i][sarake]
        #print(f"pysty: {merkit}")
        if EMPTY + pelaaja * 4 + EMPTY in merkit and EMPTY + pelaaja * 4 +EMPTY not in merkit2:
            tilanteen_arvo += 200
        if (EMPTY + pelaaja * 4 in merkit and EMPTY + pelaaja * 4 not in merkit2) or (pelaaja * 4 + EMPTY in merkit and pelaaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo += 150
        if EMPTY + pelaaja * 3 + EMPTY in merkit and EMPTY + pelaaja * 3 + EMPTY not in merkit2:
            tilanteen_arvo += 100
        if (EMPTY + pelaaja * 3 in merkit and EMPTY + pelaaja * 3 not in merkit2) or (pelaaja * 3 + EMPTY in merkit and pelaaja * 3 + EMPTY not in merkit2):
            tilanteen_arvo += 70
        if EMPTY + vastustaja * 4 + EMPTY in merkit and EMPTY + vastustaja * 4 + EMPTY not in merkit2:
            tilanteen_arvo -= 200
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 150
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 70
        if EMPTY + vastustaja * 3 + EMPTY in merkit:
            tilanteen_arvo -= 100
        merkit = ""
        merkit2 = ""

        i = rivi - min(rivi, sarake)
        j = sarake - min(rivi, sarake)
        for k in range(1, 5):
            merkit += ruudut[i - k][j - k]
            merkit2 += ruudut[i - k][j - k]
        #print(f"diag ylös: {merkit}")
        if EMPTY + pelaaja * 4 + EMPTY in merkit and EMPTY + pelaaja * 4 +EMPTY not in merkit2:
            tilanteen_arvo += 200
        if (EMPTY + pelaaja * 4 in merkit and EMPTY + pelaaja * 4 not in merkit2) or (pelaaja * 4 + EMPTY in merkit and pelaaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo += 150
        if EMPTY + pelaaja * 3 + EMPTY in merkit and EMPTY + pelaaja * 3 + EMPTY not in merkit2:
            tilanteen_arvo += 100
        if (EMPTY + pelaaja * 3 in merkit and EMPTY + pelaaja * 3 not in merkit2) or (pelaaja * 3 + EMPTY in merkit and pelaaja * 3 + EMPTY not in merkit2):
            tilanteen_arvo += 70
        if EMPTY + vastustaja * 4 + EMPTY in merkit and EMPTY + vastustaja * 4 + EMPTY not in merkit2:
            tilanteen_arvo -= 200
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 150
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 70
        if EMPTY + vastustaja * 3 + EMPTY in merkit:
            tilanteen_arvo -= 100
        merkit = ""
        merkit2 = ""

        i = min(sarake, 19 - rivi)
        j = min(rivi, 19 - sarake)
        for k in range(1, 5):
            merkit += ruudut[i - k][j + k]
            merkit2 += ruudut[i - k][j + k]
        #print(f" diag alas: {merkit}")
        if EMPTY + pelaaja * 4 + EMPTY in merkit and EMPTY + pelaaja * 4 +EMPTY not in merkit2:
            tilanteen_arvo += 200
        if (EMPTY + pelaaja * 4 in merkit and EMPTY + pelaaja * 4 not in merkit2) or (pelaaja * 4 + EMPTY in merkit and pelaaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo += 150
        if EMPTY + pelaaja * 3 + EMPTY in merkit and EMPTY + pelaaja * 3 + EMPTY not in merkit2:
            tilanteen_arvo += 100
        if (EMPTY + pelaaja * 3 in merkit and EMPTY + pelaaja * 3 not in merkit2) or (pelaaja * 3 + EMPTY in merkit and pelaaja * 3 + EMPTY not in merkit2):
            tilanteen_arvo += 70
        if EMPTY + vastustaja * 4 + EMPTY in merkit and EMPTY + vastustaja * 4 + EMPTY not in merkit2:
            tilanteen_arvo -= 200
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 150
        if (EMPTY + vastustaja * 4 in merkit and EMPTY + vastustaja * 4 not in merkit2) or (vastustaja * 4 + EMPTY in merkit and vastustaja * 4 + EMPTY not in merkit2):
            tilanteen_arvo -= 70
        if EMPTY + vastustaja * 3 + EMPTY in merkit:
            tilanteen_arvo -= 100

        #print(f"Rivi: {rivi}, sarake: {sarake}, pisteet: {tilanteen_arvo}")
        #if rivi == 0:
            #print(siirto, tilanteen_arvo)
            #print(self.mahdolliset_siirrot)
        return tilanteen_arvo
    

    def alphabeta(self, a, b, pelilauta, siirto, mahdolliset_siirrot, syvyys, maksimoi):

        if self.etsi_voittajaa(siirto, PLAYER, pelilauta):
            return -inf
        if self.etsi_voittajaa(siirto, COMPUTER, pelilauta):
            return inf
        if syvyys == 0:
            return self.arvioi_pelitilanne(pelilauta, siirto)
        if self.etsi_tasapeli(self.siirrot):
            return 0


        if maksimoi:
            max_arvo = -inf
            siirtolistan_kopio = mahdolliset_siirrot.copy()
            try:
                lauta_kopio = pelilauta.ruudukko.copy()
            except:
                lauta_kopio = pelilauta.copy()
            for siirto_tuple in mahdolliset_siirrot:
                lauta_kopio[siirto_tuple[0]][siirto_tuple[1]] = COMPUTER
                self.etsi_mahdolliset_siirrot(siirto_tuple, siirtolistan_kopio)
                arvo = self.alphabeta(a, b, lauta_kopio, siirto_tuple, siirtolistan_kopio, syvyys - 1, False)
                lauta_kopio[siirto_tuple[0]][siirto_tuple[1]] = EMPTY
                max_arvo = max(max_arvo, arvo)
                if max_arvo > b:
                    break
                a = max(a, max_arvo)
            return max_arvo

        else:
            min_arvo = inf
            siirtolistan_kopio = mahdolliset_siirrot.copy()
            try:
                lauta_kopio = pelilauta.ruudukko.copy()
            except:
                lauta_kopio = pelilauta.copy()
            for siirto_tuple in mahdolliset_siirrot:
                lauta_kopio[siirto_tuple[0]][siirto_tuple[1]] = PLAYER
                self.etsi_mahdolliset_siirrot(siirto_tuple, siirtolistan_kopio)
                arvo = self.alphabeta(a, b, lauta_kopio, siirto_tuple, siirtolistan_kopio, syvyys - 1, True)
                lauta_kopio[siirto_tuple[0]][siirto_tuple[1]] = EMPTY
                min_arvo = min(min_arvo, arvo)
                if min_arvo < a:
                    break
                b = min(b, min_arvo)
            return min_arvo

    def etsi_paras_siirto(self, mahdolliset_siirrot, pelilauta):
        paras_arvo = -inf
        paras_siirto = choice(list(mahdolliset_siirrot))

        for siirto in mahdolliset_siirrot:
            siirron_arvo = \
                self.alphabeta(-inf, inf, pelilauta, siirto, mahdolliset_siirrot, 2, True)

            if siirron_arvo > paras_arvo:
                paras_siirto = siirto
                paras_arvo = siirron_arvo

            elif siirron_arvo == -inf:
                paras_siirto = siirto
                paras_arvo = siirron_arvo

        return paras_siirto
