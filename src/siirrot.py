from math import inf
from ruudukko import Ruudukko

class Peli:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False
        self.siirto = None

    def tarkista_siirto(self, siirto):
        self.virhe = False
        viesti = "Koordinaatti väärässsä muodossa"
        if len(siirto) > 3 or len(siirto) < 2:
            self.virhe = True
            print(viesti)
        elif siirto[0] not in "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst":
            self.virhe = True
            print(viesti)
        elif siirto[1:] not in "1011121314151617181920" or int(siirto[1:]) not in range(1, 21):
            self.virhe = True
            print(viesti)
        return self.virhe


    def pelaa(self):
        voittaja = None
        while True:
            self.pelilauta.tulosta_ruudukko()

            siirto = input("Valitse koordinaatit (esim. A1):")
            if not self.tarkista_siirto(siirto):
                self.siirto = self.muuta_koordinaateiksi(siirto)
                if self.pelilauta.ruudukko[self.siirto[0]][self.siirto[1]] == "-":
                    self.pelilauta.ruudukko[self.siirto[0]][self.siirto[1]] = "X"
                    if self.etsi_voittajaa(self.siirto, "X"):
                        voittaja = "X"
                        break

            self.siirto = self.paras_siirto()
            print("Tietokoneen vuoro")
            if self.pelilauta.ruudukko[self.siirto[0]][self.siirto[1]] == "-":
                self.pelilauta.ruudukko[self.siirto[0]][self.siirto[1]] = "O"
                if self.etsi_voittajaa(self.siirto, "O"):
                    voittaja = "O"
                    break

        print(f"Voittaja on {voittaja}")

    def etsi_voittajaa(self, siirto, pelaaja):
        koord = self.muuta_koordinaateiksi(siirto)
        i = koord[0]
        j = koord[1]
        ruudut = self.pelilauta.ruudukko
        merkkijono1 = ""
        merkkijono2 = ""
        merkkijono3 = ""
        merkkijono4 = ""
        for x in range(20):
            merkkijono1 += ruudut[x][j]
        for y in range(20):
            merkkijono2 += ruudut[i][y]
        if self.etsi_rivi(merkkijono1, pelaaja) != -1 or self.etsi_rivi(merkkijono2, pelaaja) != -1:
            return True
        diagonaali_i = i - min(i, j)
        diagonaali_j = j - min(i, j)
        for k in range(20 - max(diagonaali_i, diagonaali_j)):
            merkkijono3 += ruudut[diagonaali_i + k][diagonaali_j + k]
        diagonaali_i = i + min(19 - i, j)
        diagonaali_j = j - min(19 - i, j)
        for k in range(20 - max(19 - diagonaali_i, diagonaali_j)):
            merkkijono4 += ruudut[diagonaali_i - k][diagonaali_j + k]
        if self.etsi_rivi(merkkijono3, pelaaja) != -1 or self.etsi_rivi(merkkijono4, pelaaja) != -1:
            return True
        return False

    def vapaat_ruudut(self):
        vapaat_ruudut = []
        for i in range(20):
            for j in range(20):
                if self.pelilauta.ruudukko[i][j] == "-":
                    vapaat_ruudut.append((i, j))
        return vapaat_ruudut

    def etsi_rivi(self, merkit, pelaaja):
        voitto = pelaaja * 5
        return merkit.find(voitto)

    def muuta_koordinaateiksi(self, siirto):
        try:
            sarake = ord(siirto[0].lower()) - 97
            rivi = int(siirto[1:]) - 1
            return (rivi, sarake)
        except:
            return siirto

    def minmax(self, pelilauta, syvyys, maksimoi):
        # arvot = {"X": 1, "O": -1}

        if self.etsi_voittajaa(self.siirto, "X"):
            return -inf
        elif self.etsi_voittajaa(self.siirto, "O"):
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

    def paras_siirto(self):
        paras_arvo = -inf
        paras_siirto = None

        for i, j in self.vapaat_ruudut():
            self.pelilauta.ruudukko[i][j] = "O"
            siirron_arvo = self.minmax(self.pelilauta.ruudukko, 0, False)
            self.pelilauta.ruudukko[i][j] = "-"

            if siirron_arvo > paras_arvo:
                paras_siirto = (i, j)
                paras_arvo = siirron_arvo

        return paras_siirto
