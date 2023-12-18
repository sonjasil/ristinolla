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