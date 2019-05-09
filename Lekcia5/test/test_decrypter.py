from unittest import TestCase
from Lekcia5.decrypter import *


class TestDecrypter(TestCase):
    def test_decrypter_aaa(self):
        self.assertEqual(decrypter("aaa", 1), "zzz")

    def test_decrypter_random(self):
        self.assertEqual(decrypter("zzz", 1), "yyy")

    def test_decrypter_26(self):
        self.assertEqual(decrypter("aaa", 26), "aaa")

    def test_decrypter_0(self):
        self.assertEqual(decrypter("aaa", 0), "aaa")

    def test_decrypter_non(self):
        self.assertEqual(decrypter("a1a", 1), "z1z")

    def test_decrypter_whitespace(self):
        self.assertEqual(decrypter("a a a", 2), "y y y")
