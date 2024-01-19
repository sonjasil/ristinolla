from math import inf
from random import choice
from ruudukko import Ruudukko

PLAYER = "X"
COMPUTER = "O"
EMPTY = "-"

class Peli:
    def __init__(self):
        self.pelilauta = Ruudukko()
        self.mahdolliset_siirrot = set()
        self.siirrot = 0

    def tarkista_siirto(self, rivi, sarake):
        virhe = False
        if not rivi.isnumeric() or not sarake.isnumeric():
            virhe = True
            print("Väärä koordinaatti")
        elif int(rivi) not in range(1, 21) or int(sarake) not in range(1, 21):
            virhe = True
            print("Väärä koordinaatti")
        return virhe

    def tee_siirto(self, siirto, pelaaja):
        self.pelilauta.ruudukko[siirto[0]][siirto[1]] = pelaaja
        self.siirrot += 1

    def pelaa(self):
        voittaja = None
        while True:
            self.pelilauta.tulosta_ruudukko()
            print(self.mahdolliset_siirrot)

            while True:
                rivi = input(("Valitse rivi 1-20: "))
                sarake = input("Valitse sarake 1-20: ")
                if not self.tarkista_siirto(rivi, sarake):
                    break
            siirto = (int(rivi) - 1, int(sarake) - 1)
            if self.pelilauta.ruudukko[siirto[0]][siirto[1]] == EMPTY:
                self.tee_siirto(siirto, PLAYER)
                self.etsi_mahdolliset_siirrot(siirto, self.mahdolliset_siirrot)
                if self.etsi_voittajaa(siirto, PLAYER, self.pelilauta):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = PLAYER
                    break

            ai_siirto = self.etsi_paras_siirto(self.mahdolliset_siirrot, self.pelilauta)
            self.etsi_mahdolliset_siirrot(ai_siirto, self.mahdolliset_siirrot)
            print("Tietokoneen vuoro")
            if self.pelilauta.ruudukko[ai_siirto[0]][ai_siirto[1]] == EMPTY:
                self.tee_siirto(ai_siirto, COMPUTER)
                if self.etsi_tasapeli(self.siirrot):
                    break
                if self.etsi_voittajaa(ai_siirto, COMPUTER, self.pelilauta):
                    self.pelilauta.tulosta_ruudukko()
                    voittaja = COMPUTER
                    break
        if voittaja is not None:
            print(f"Voittaja on {voittaja}")
        else:
            print("Tasapeli")

    def etsi_voittajaa(self, siirto, pelaaja, pelilauta):
        rivi = siirto[0]
        sarake = siirto[1]
        laskuri = 0
        ruudut = pelilauta.ruudukko

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

        for i in range(rivi - 1, max(-1, rivi - 3), -1):
            if ruudut[i][sarake] == EMPTY:
                mahdolliset_siirrot.add((i, sarake))

        for i in range(rivi + 1, min(20, rivi + 3)):
            if ruudut[i][sarake] == EMPTY:
                mahdolliset_siirrot.add((i, sarake))

        for j in range(sarake - 1, max(-1, sarake - 3), -1):
            if ruudut[rivi][j] == EMPTY:
                mahdolliset_siirrot.add((rivi, j))

        for j in range(sarake + 1, min(20, sarake + 3)):
            if ruudut[rivi][j] == EMPTY:
                mahdolliset_siirrot.add((rivi, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake - k
            if i < 0 or j < 0:
                break
            if ruudut[i][j] == EMPTY:
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake + k
            if i > 19 or j > 19:
                break
            if ruudut[i][j] == EMPTY:
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi - k
            j = sarake + k
            if i < 0 or j > 19:
                break
            if ruudut[i][j] == EMPTY:
                mahdolliset_siirrot.add((i, j))

        for k in range(1, 3):
            i = rivi + k
            j = sarake - k
            if i > 19 or j < 0:
                break
            if ruudut[i][j] == EMPTY:
                mahdolliset_siirrot.add((i, j))

        if siirto in mahdolliset_siirrot:
            mahdolliset_siirrot.remove(siirto)


    def etsi_tasapeli(self, siirtomaara):
        if siirtomaara == 400:
            return True
        return False

    def arvioi_osan_arvo(self, osa):
        osan_arvo = 0
        pelaaja = COMPUTER
        vastustaja = PLAYER

        pelaajan_merkit = osa.count(pelaaja)
        vastustajan_merkit = osa.count(vastustaja)
        tyhjat_merkit = osa.count(EMPTY)

        if pelaajan_merkit == 4:
            osan_arvo += 3000
        if vastustajan_merkit == 4 and pelaajan_merkit == 1:
            osan_arvo += 2500
        if pelaajan_merkit == 3 and tyhjat_merkit == 2:
            osan_arvo += 2000
        if vastustajan_merkit == 3 and pelaajan_merkit >= 1:
            osan_arvo += 3500
        if pelaajan_merkit == 3 and tyhjat_merkit == 1:
            osan_arvo += 150
        if pelaajan_merkit == 2 and tyhjat_merkit == 3:
            osan_arvo += 100
        if pelaajan_merkit == 2 and tyhjat_merkit < 3:
            osan_arvo += 50

        if vastustajan_merkit == 4 and tyhjat_merkit == 1:
            osan_arvo -= 400
        if vastustajan_merkit == 3 and tyhjat_merkit == 2:
            osan_arvo -= 300
        if vastustajan_merkit == 3 and tyhjat_merkit == 1:
            osan_arvo -= 250
        if vastustajan_merkit == 2 and tyhjat_merkit == 3:
            osan_arvo -= 200
        if vastustajan_merkit == 2 and tyhjat_merkit < 3:
            osan_arvo -= 150

        return osan_arvo

    def arvioi_pelitilanne(self, pelilauta, siirto):
        tilanteen_arvo = 0
        rivi = siirto[0]
        sarake = siirto[1]
        ruudut = pelilauta.ruudukko

        for i in range(5):
            alku = sarake - i
            loppu = alku + 5
            if alku < 0 or loppu > 19:
                break
            osa = ruudut[rivi][alku:loppu]
            if self.arvioi_osan_arvo(osa) > tilanteen_arvo:
                tilanteen_arvo = self.arvioi_osan_arvo(osa)

        for i in range(5):
            alku = rivi - i
            loppu = alku + 5
            if alku < 0 or loppu > 19:
                break
            osa = []
            for r in range(alku, loppu):
                osa.append(ruudut[r][sarake])
            if self.arvioi_osan_arvo(osa) > tilanteen_arvo:
                tilanteen_arvo = self.arvioi_osan_arvo(osa)

        for i in range(5):
            alkurivi = rivi - i
            alkusarake = sarake - i
            if alkurivi < 0 or alkusarake < 0:
                break
            osa = []
            for k in range(5):
                r = alkurivi + k
                s = alkusarake + k
                if r > 19 or s > 19:
                    break
                osa.append(ruudut[r][s])
            if self.arvioi_osan_arvo(osa) > tilanteen_arvo:
                tilanteen_arvo = self.arvioi_osan_arvo(osa)

        for i in range(5):
            alkurivi = rivi + i
            alkusarake = sarake - i
            osa = []
            if alkurivi > 19 or alkusarake < 0:
                break
            for k in range(5):
                r = alkurivi - k
                s = alkusarake + k
                if r < 0 or s > 19:
                    break
                osa.append(ruudut[r][s])
            if self.arvioi_osan_arvo(osa) > tilanteen_arvo:
                tilanteen_arvo = self.arvioi_osan_arvo(osa)

        return tilanteen_arvo

    def alphabeta(self, alpha, beta, pelilauta, siirto, mahdolliset_siirrot, syvyys, maksimoi):

        if maksimoi:
            if self.etsi_voittajaa(siirto, PLAYER, pelilauta):
                return -inf
            if self.etsi_tasapeli(self.siirrot):
                return 0
            if syvyys == 0:
                return self.arvioi_pelitilanne(pelilauta, siirto)
            max_arvo = -inf
            for siirto_tuple in mahdolliset_siirrot:
                siirtolistan_kopio = mahdolliset_siirrot.copy()
                self.etsi_mahdolliset_siirrot(siirto_tuple, siirtolistan_kopio)
                pelilauta.ruudukko[siirto_tuple[0]][siirto_tuple[1]] = COMPUTER
                arvo = self.alphabeta(alpha, beta, pelilauta, siirto_tuple, siirtolistan_kopio, syvyys - 1, False)
                pelilauta.ruudukko[siirto_tuple[0]][siirto_tuple[1]] = EMPTY
                max_arvo = max(max_arvo, arvo)
                if max_arvo > beta:
                    break
                alpha = max(alpha, max_arvo)
            return max_arvo

        else:
            if self.etsi_voittajaa(siirto, COMPUTER, pelilauta):
                return inf
            if self.etsi_tasapeli(self.siirrot):
                return 0
            if syvyys == 0:
                return self.arvioi_pelitilanne(pelilauta, siirto)
            min_arvo = inf
            for siirto_tuple in mahdolliset_siirrot:
                siirtolistan_kopio = mahdolliset_siirrot.copy()
                self.etsi_mahdolliset_siirrot(siirto_tuple, siirtolistan_kopio)
                pelilauta.ruudukko[siirto_tuple[0]][siirto_tuple[1]] = PLAYER
                arvo = self.alphabeta(alpha, beta, pelilauta, siirto_tuple, siirtolistan_kopio, syvyys - 1, True)
                pelilauta.ruudukko[siirto_tuple[0]][siirto_tuple[1]] = EMPTY
                min_arvo = min(min_arvo, arvo)
                if min_arvo < alpha:
                    break
                beta = min(beta, min_arvo)
            return min_arvo

    def etsi_paras_siirto(self, mahdolliset_siirrot, pelilauta):
        paras_arvo = -inf
        paras_siirto = choice(list(mahdolliset_siirrot))

        for siirto in mahdolliset_siirrot:
            siirtolistan_kopio = mahdolliset_siirrot.copy()
            self.etsi_mahdolliset_siirrot(siirto, siirtolistan_kopio)
            pelilauta.ruudukko[siirto[0]][siirto[1]] = COMPUTER
            siirron_arvo = \
                self.alphabeta(-inf, inf, pelilauta, siirto, siirtolistan_kopio, 2, False)
            pelilauta.ruudukko[siirto[0]][siirto[1]] = EMPTY

            if siirron_arvo > paras_arvo:
                paras_siirto = siirto
                paras_arvo = siirron_arvo

        return paras_siirto
