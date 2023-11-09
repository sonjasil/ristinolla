from ruudukko import Ruudukko

class Siirto:
    def __init__(self):
        self.pelilauta = Ruudukko()

    def tee_siirto(self):
        for i in range(400):
            self.pelilauta.tulosta_ruudukko()
            siirto = input("Valitse koordinaatit (esim. A1):")
            if len(siirto) != 2:
                break
            if siirto[0] not in "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst":
                break
            if int(siirto[1]) not in range(1, 21):
                break
            else:
                sarake = ord(siirto[0].lower()) - 97
                rivi = int(siirto[1]) - 1
                if i % 2 == 0:
                    self.pelilauta.ruudukko[rivi][sarake] = "X"
                elif i % 2 != 0:
                    self.pelilauta.ruudukko[rivi][sarake] = "O"
                i += 1
        print("Koordinaatti väärässä muodossa")

peli = Siirto()
peli.tee_siirto()