from unittest import TestCase
# zmenit import aby sedel na zadanie.py
from Lekcia6.rc_validator import rc_validator


class TestRcValidator(TestCase):
    def test_rc_validator_valid_zero_2(self):
        self.assertTrue(rc_validator("000102984"))

    def test_rc_validator_valid_zero_1(self):
        self.assertTrue(rc_validator("010102984"))

    def test_rc_validator_valid_zero_2_10(self):
        self.assertTrue(rc_validator("0002097315"))

    def test_rc_validator_valid(self):
        self.assertTrue(rc_validator("8302167335"))

    def test_rc_validator_valid(self):
        self.assertTrue(rc_validator("8352167329"))

    def test_rc_validator_valid_pre54_male(self):
        self.assertTrue(rc_validator("520410453"))

    def test_rc_validator_valid_pre54_female(self):
        self.assertTrue(rc_validator("525410453"))

    def test_rc_validator_valid_slash(self):
        self.assertTrue(rc_validator("830216/7335"))

    def test_rc_validator_valid_slash(self):
        self.assertTrue(rc_validator("835216/7329"))

    def test_rc_validator_valid_pre54_male_slash(self):
        self.assertTrue(rc_validator("520410/453"))

    def test_rc_validator_valid_pre54_female_slash(self):
        self.assertTrue(rc_validator("525410/453"))

    def test_rc_validator_invalid_female(self):
        self.assertFalse(rc_validator("8451307341"))

    def test_rc_validator_invalid_male(self):
        self.assertFalse(rc_validator("8401307341"))

    def test_rc_validator_invalid_female_slash(self):
        self.assertFalse(rc_validator("845130/7341"))

    def test_rc_validator_invalid_male_slash(self):
        self.assertFalse(rc_validator("840130/7341"))

    def test_rc_validator_invalid_male_bad_date(self):
        self.assertFalse(rc_validator("8302297322"))

    def test_rc_validator_invalid_female_bad_date(self):
        self.assertFalse(rc_validator("8352297329"))

    def test_rc_validator_invalid_bad_date(self):
        self.assertFalse(rc_validator("8213307234"))

    def test_rc_validator_bad_input(self):
        self.assertFalse(rc_validator("abc"))

    def test_rc_validator_bad_input_numeric(self):
        self.assertFalse(rc_validator(15))

    def test_rc_validator_bad_rc_post54_9digits(self):
        self.assertFalse(rc_validator("830214324"))

# test disabled po urcitu dobu
#    def test_rc_validator_bad_rc_pre54_l0digits(self):
#        self.assertFalse(rc_validator("5301167322"))
