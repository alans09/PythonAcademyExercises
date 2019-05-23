from unittest import TestCase
from Lekcia5.funkcie_zaklad import spocitaj

class TestSpocitaj(TestCase):
    def test_spocitaj_valid(self):
        self.assertEqual(spocitaj(1, 2), 3)

    def test_spocitaj_string(self):
        self.assertFalse(spocitaj("a", "b"))

    def test_spocitaj_zero(self):
        self.assertEqual(spocitaj(0, 0), 0)
