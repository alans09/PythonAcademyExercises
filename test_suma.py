from unittest import TestCase
import untest

class TestSuma(TestCase):
    def test_suma(self):
        self.assertEqual(untest.suma(1, 2), 3)
