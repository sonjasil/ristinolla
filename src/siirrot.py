from math import inf
from ruudukko import Ruudukko

class Peli:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False

    def tarkista_siirto(self, rivi, sarake):
        self.virhe = False
        if rivi not in range(1, 20) or sarake not in range(1, 20):
            self.virhe = True
            print("Väärä koordinaatti")
        return self.virhe


    def pelaa(self):
        voittaja = None
        while True:
            self.pelilauta.tulosta_ruudukko()

            rivi = int(input(("Valitse rivi 1-20: ")))
            sarake = int(input("Valitse sarake 1-20: "))
            siirto = (rivi - 1, sarake - 1)
            if not self.tarkista_siirto(rivi, sarake):
                if self.pelilauta.ruudukko[siirto[0]][siirto[1]] == "-":
                    self.pelilauta.ruudukko[siirto[0]][siirto[1]] = "X"
                    if self.etsi_voittajaa(siirto, "X"):
                        self.pelilauta.tulosta_ruudukko()
                        voittaja = "X"
                        break

            ai_siirto = self.etsi_paras_siirto(siirto)
            print("Tietokoneen vuoro")
            if self.pelilauta.ruudukko[ai_siirto[0]][ai_siirto[1]] == "-":
                self.pelilauta.ruudukko[ai_siirto[0]][ai_siirto[1]] = "O"
                if self.etsi_voittajaa(ai_siirto, "O"):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = "O"
                    break

        print(f"Voittaja on {voittaja}")

    def etsi_voittajaa(self, siirto, pelaaja):
        x = siirto[0]
        y = siirto[1]
        laskuri1 = 0
        laskuri2 = 0
        ruudut = self.pelilauta.ruudukko
        for i in range(max(0, x - 1), max(0, x - 4), -1):
            print(f"1. s: i = {i}, x = {x}, y = {y}")
            if ruudut[i][y] == ruudut[i + 1][y] and i != i + 1 and ruudut[i][y] == pelaaja:
                laskuri1 += 1
                print(f"laskuri1: {laskuri1}")
        for i in range(min(0, x + 1), min(20, x + 4)):
            print(f"2. s: i = {i}, x = {x}, y = {y}")
            if ruudut[i][y] == ruudut[i - 1][y] and i != i - 1 and ruudut[i][y] == pelaaja:
                laskuri2 += 1
                print(f"laskuri2: {laskuri2}")
        print(f"summa: {laskuri1 + laskuri2 + 1}")
        input("Press Enter")
        if laskuri1 + laskuri2 + 1 >= 5:
            return True
        return False

    def vapaat_ruudut(self):
        vapaat_ruudut = []
        for i in range(20):
            for j in range(20):
                if self.pelilauta.ruudukko[i][j] == "-":
                    vapaat_ruudut.append((i, j))
        return vapaat_ruudut
        
    def minmax(self, pelilauta, siirto, syvyys, maksimoi):
        # arvot = {"X": 1, "O": -1}

        if self.etsi_voittajaa(siirto, "X"):
            return -inf
        elif self.etsi_voittajaa(siirto, "O"):
            return inf
        elif syvyys == 0:
            return 0

        if maksimoi:
            max_arvo = -inf
            for i, j in self.vapaat_ruudut():
                pelilauta[i][j] = "O"
                arvo = self.minmax(pelilauta, syvyys + 1, False)
                pelilauta[i][j] = "-"
                max_arvo = max(max_arvo, arvo)
            return max_arvo

        else:
            min_arvo = inf
            for i, j in self.vapaat_ruudut():
                pelilauta[i][j] = "X"
                arvo = self.minmax(pelilauta, syvyys + 1, True)
                pelilauta[i][j] = "-"
                min_arvo = min(min_arvo, arvo)
            return min_arvo

    def etsi_paras_siirto(self, edellinen_siirto):
        paras_arvo = -inf
        paras_siirto = None

        for i, j in self.vapaat_ruudut():
            self.pelilauta.ruudukko[i][j] = "O"
            siirron_arvo = self.minmax(self.pelilauta.ruudukko, edellinen_siirto, 0, False)
            self.pelilauta.ruudukko[i][j] = "-"

            if siirron_arvo > paras_arvo:
                paras_siirto = (i, j)
                paras_arvo = siirron_arvo

        return paras_siirto
