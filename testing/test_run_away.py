from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import run_away


class TestRunAway(TestCase):
    @patch('builtins.input', side_effect=['3'])
    @patch('random.randrange', return_value=1)
    def test_run_away_incorrect_guess(self, _, __):
        result = run_away()
        self.assertEqual(result, -1)

    @patch('builtins.input', side_effect=['4'])
    @patch('random.randrange', return_value=4)
    def test_run_away_correct_guess(self, _, __):
        result = run_away()
        self.assertEqual(result, 0)

    @patch('builtins.input', side_effect=['abc'])
    @patch('random.randrange', return_value=4)
    def test_run_away_invalid_guess(self, _, __):
        result = run_away()
        self.assertEqual(result, -1)

