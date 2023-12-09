from unittest import TestCase
from unittest.mock import patch
import io
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
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one_invalid_input(self, mock_output, _):
        actual = combat_choice()
        expected = 1
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Invalid input! You must input a number 1, 2, or 3. Try again.\n'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['?', '2.3', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_many_invalid_input(self, mock_output, _):
        actual = combat_choice()
        expected = 1
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Invalid input! You must input a number 1, 2, or 3. Try again.\n'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)