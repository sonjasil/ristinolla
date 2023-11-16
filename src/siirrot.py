from ruudukko import Ruudukko

class Siirto:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.virhe = False

    def tarkista_siirto(self, siirto):
        self.virhe = False
        viesti = "Koordinaatti väärässsä muodossa"
        if len(siirto) != 2:
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
            if self.tarkista_siirto(siirto) == False:
                paikka = self.muuta_koordinaateiksi(siirto)
                if i % 2 == 0 and self.pelilauta.ruudukko[paikka[1]][paikka[0]] == "-":
                    self.pelilauta.ruudukko[paikka[1]][paikka[0]] = "X"
                elif i % 2 != 0 and self.pelilauta.ruudukko[paikka[1]][paikka[0]] == "-":
                    self.pelilauta.ruudukko[paikka[1]][paikka[0]] = "O"
                i += 1

    #def etsi_voittajaa(self, siirto):
        
    def muuta_koordinaateiksi(self, siirto):
        sarake = ord(siirto[0].lower()) - 97
        rivi = int(siirto[1]) - 1
        return (sarake, rivi)