import unittest
from ruudukko import Ruudukko

class TestRuudukko(unittest.TestCase):
    def setUp(self):
        self.ruudukko = Ruudukko().ruudukko

    def test_ruudukon_korkeus(self):
        self.assertAlmostEqual(len(self.ruudukko), 20)

    def test_ruudukon_leveys(self):
        self.assertAlmostEqual(len(self.ruudukko[0]), 20)
