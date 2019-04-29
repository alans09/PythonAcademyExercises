import unittest


def suma(a, b):
    if isinstance(a, str):
        raise AssertionError
    return a + b


class TestSuma(unittest.TestCase):
    def test_good(self):
        self.assertEqual(suma(1, 2), 3)

    def test_assertion(self):
        with self.assertRaises(TypeError):
            suma("a", 4)
