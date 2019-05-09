from unittest import TestCase
import random


def vydel(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        raise


class TestVydel(TestCase):
    def test_basic(self):
        self.assertEqual(vydel(1, 1), 1)

    def test_exception(self):
        self.assertRaises(ZeroDivisionError, vydel, 1, 0)

    def test_exception_other(self):
        with self.assertRaises(ZeroDivisionError) as exc:
            vydel(1, 0)
        exception = exc.exception
        self.assertEqual(exception.args, ("division by zero",))
