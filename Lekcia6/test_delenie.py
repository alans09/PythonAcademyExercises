from unittest import TestCase
from Lekcia6.vynimky import delenie

class TestDelenie(TestCase):
    def test_delenie(self):
        self.assertRaises(ZeroDivisionError, delenie, 2, 0)
