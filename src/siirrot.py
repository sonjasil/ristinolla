from ruudukko import Ruudukko

class Siirto:
    def __init__(self):
        self.pelilauta = Ruudukko()

    def tee_siirto(self):
        virhe = "Koordinaatti väärässä muodossa"
        for i in range(400):
            self.pelilauta.tulosta_ruudukko()
            siirto = input("Valitse koordinaatit (esim. A1):")
            if len(siirto) != 2:
                print(virhe)
                continue
            if siirto[0] not in "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst":
                print(virhe)
                continue
            if int(siirto[1]) not in range(1, 21):
                print(virhe)
                continue
            else:
                paikka = self.muuta_koordinaateiksi(siirto)
                if i % 2 == 0:
                    self.pelilauta.ruudukko[paikka[1]][paikka[0]] = "X"
                elif i % 2 != 0:
                    self.pelilauta.ruudukko[paikka[1]][paikka[0]] = "O"
                i += 1

    #def etsi_voittajaa(self, siirto):
        
    def muuta_koordinaateiksi(self, siirto):
        sarake = ord(siirto[0].lower()) - 97
        rivi = int(siirto[1]) - 1
        return (sarake, rivi)