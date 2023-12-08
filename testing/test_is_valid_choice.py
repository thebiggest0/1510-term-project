from unittest import TestCase
from character_actions.combat import is_valid_choice


class TestValidChoice(TestCase):
    def test_valid_choice_1(self):
        actual = is_valid_choice('1')
        self.assertTrue(actual)

    def test_valid_choice_2(self):
        actual = is_valid_choice('2')
        self.assertTrue(actual)

    def test_valid_choice_3(self):
        actual = is_valid_choice('3')
        self.assertTrue(actual)

    def test_invalid_choice_float(self):
        actual = is_valid_choice('1.222')
        self.assertFalse(actual)

    def test_invalid_choice_string(self):
        actual = is_valid_choice('uuu')
        self.assertFalse(actual)