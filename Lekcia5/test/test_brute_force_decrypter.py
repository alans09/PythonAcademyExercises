from unittest import TestCase
from Lekcia5.decrypter import *


class TestBruteForceDecrypter(TestCase):
    def test_brute_force_decrypter(self):
        self.assertIn("Na svete existuju dva druhy programatorov. Ti co programuju v Pythone a ti co sa mylia.",
                      brute_force_decrypter(MESSAGE))

    def test_brute_force_decrypter_none(self):
        self.assertNotIn("Na svete existuju dva druhy programatorov. Ti co programuju v Pythone a ti co sa mylia",
                         brute_force_decrypter(MESSAGE))

    def test(self):
        self.assert