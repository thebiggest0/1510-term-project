from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import combat_choice


class TestCombatChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_user_choice_1(self, _):
        actual = combat_choice()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['2'])
    def test_user_choice_2(self, _):
        actual = combat_choice()
        expected = 2
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['3'])
    def test_user_choice_3(self, _):
        actual = combat_choice()
        expected = 3
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['?', '1'])
    def test_one_invalid_input(self, _):
        actual = combat_choice()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['?', '2.3', '1'])
    def test_many_invalid_input(self, _):
        actual = combat_choice()
        expected = 1
        self.assertEqual(actual, expected)