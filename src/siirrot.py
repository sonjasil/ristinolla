from ruudukko import Ruudukko

class Siirto:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False

    def tarkista_siirto(self, siirto):
        self.virhe = False
        viesti = "Koordinaatti väärässsä muodossa"
        if len(siirto) > 3 or len(siirto) < 2:
            self.virhe = True
            print(viesti)
        elif siirto[0] not in "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst":
            self.virhe = True
            print(viesti)
        elif int(siirto[1]) not in range(1, 21):
            self.virhe = True
            print(viesti)
        return self.virhe


    def tee_siirto(self):
        i = 0
        while i < 400:
            self.pelilauta.tulosta_ruudukko()
            siirto = input("Valitse koordinaatit (esim. A1):")
            if not self.tarkista_siirto(siirto):
                paikka = self.muuta_koordinaateiksi(siirto)
                if i % 2 == 0 and self.pelilauta.ruudukko[paikka[0]][paikka[1]] == "-":
                    self.pelilauta.ruudukko[paikka[0]][paikka[1]] = "X"
                    print(self.etsi_voittajaa(siirto, "X"))
                elif i % 2 != 0 and self.pelilauta.ruudukko[paikka[0]][paikka[1]] == "-":
                    self.pelilauta.ruudukko[paikka[0]][paikka[1]] = "O"
                    print(self.etsi_voittajaa(siirto, "O"))
                i += 1

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
            print(diagonaali_i - k, diagonaali_j + k)
        if self.etsi_rivi(merkkijono3, pelaaja) != -1 or self.etsi_rivi(merkkijono4, pelaaja) != -1:
            return True

    def etsi_rivi(self, merkit, pelaaja):
        voitto = pelaaja * 5
        return merkit.find(voitto)


    def muuta_koordinaateiksi(self, siirto):
        sarake = ord(siirto[0].lower()) - 97
        rivi = int(siirto[1:]) - 1
        return (rivi, sarake)
