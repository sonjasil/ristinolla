import unittest
from siirrot import Peli

class TestPeli(unittest.TestCase):
    def setUp(self):
        self.peli = Peli()
        self.ruudukko = self.peli.pelilauta.ruudukko

    def test_etsi_voittajaa_vaakarivi(self):
        self.peli.tee_siirto((0, 0), "X")
        self.peli.tee_siirto((0, 1), "X")
        self.peli.tee_siirto((0, 2), "X")
        self.peli.tee_siirto((0, 3), "X")
        self.peli.tee_siirto((0, 4), "X")

        self.assertEqual(self.peli.etsi_voittajaa((0, 4), "X", self.ruudukko), True)

    def test_etsi_voittajaa_pystyrivi(self):
        self.peli.tee_siirto((1, 3), "X")
        self.peli.tee_siirto((2, 3), "X")
        self.peli.tee_siirto((3, 3), "X")
        self.peli.tee_siirto((4, 3), "X")
        self.peli.tee_siirto((5, 3), "X")

        self.assertEqual(self.peli.etsi_voittajaa((5, 3), "X", self.ruudukko), True)

    def test_etsi_voittajaa_diagonaali_alas(self):
        self.peli.tee_siirto((0, 0), "X")
        self.peli.tee_siirto((1, 1), "X")
        self.peli.tee_siirto((2, 2), "X")
        self.peli.tee_siirto((3, 3), "X")
        self.peli.tee_siirto((4, 4), "X")

        self.assertEqual(self.peli.etsi_voittajaa((2, 2), "X", self.ruudukko), True)

    def test_etsi_voittajaa_diagonaali_ylos(self):
        self.peli.tee_siirto((6, 6), "X")
        self.peli.tee_siirto((5, 7), "X")
        self.peli.tee_siirto((4, 8), "X")
        self.peli.tee_siirto((3, 9), "X")
        self.peli.tee_siirto((2, 10), "X")

        self.assertEqual(self.peli.etsi_voittajaa((3, 9), "X", self.ruudukko), True)

    def test_siirron_validointi_vaara_numero(self):
        self.assertEqual(self.peli.tarkista_siirto("21", "19"), True)

    def test_siirron_validointi_ei_numeroa(self):
        self.assertEqual(self.peli.tarkista_siirto("a", "b"), True)

    def test_etsi_mahdolliset_siirrot(self):
        peli = Peli()
        peli.tee_siirto((5, 5), "X")
        peli.etsi_mahdolliset_siirrot((5, 5), peli.mahdolliset_siirrot)
        ymparoivat_siirrot = [(2, 4), (5, 5), (6, 2), (3, 4), (4, 3), (5, 4), (4, 6), (5, 3), (6, 4), (4, 2), (4, 5), (3, 3), (2, 6), (2, 2), (6, 6), (3, 5)]

        self.assertEqual(list(peli.mahdolliset_siirrot).sort(), ymparoivat_siirrot.sort())

    def test_esta_pelaajan_voitto(self):
        peli = Peli()
        peli.tee_siirto((4, 4), "X")
        peli.etsi_mahdolliset_siirrot((4, 4), peli.mahdolliset_siirrot)
        peli.tee_siirto((2, 4), "O")
        peli.etsi_mahdolliset_siirrot((2, 4), peli.mahdolliset_siirrot)
        peli.tee_siirto((4, 5), "X")
        peli.etsi_mahdolliset_siirrot((4, 5), peli.mahdolliset_siirrot)
        peli.tee_siirto((3, 4), "O")
        peli.etsi_mahdolliset_siirrot((3, 4), peli.mahdolliset_siirrot)
        peli.tee_siirto((4, 6), "X")
        peli.etsi_mahdolliset_siirrot((4, 6), peli.mahdolliset_siirrot)
        peli.tee_siirto((4, 3), "O")
        peli.etsi_mahdolliset_siirrot((4, 3), peli.mahdolliset_siirrot)
        peli.tee_siirto((4, 7), "X")
        peli.etsi_mahdolliset_siirrot((4, 7), peli.mahdolliset_siirrot)

        paras_siirto = peli.etsi_paras_siirto(peli.mahdolliset_siirrot, peli.pelilauta)

        self.assertEqual(paras_siirto, (4, 8))