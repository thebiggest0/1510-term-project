from unittest import TestCase
from unittest.mock import patch
from game_start import difficulty_checker


class TestDifficultyChecker(TestCase):
    @patch('builtins.input', return_value='1')
    def test_difficulty_checker_easy(self, _):
        result = difficulty_checker()
        self.assertEqual(result, 1)

    @patch('builtins.input', return_value='2')
    def test_difficulty_checker_medium(self, _):
        result = difficulty_checker()
        self.assertEqual(result, 2)

    @patch('builtins.input', return_value='3')
    def test_difficulty_checker_hard(self, _):
        result = difficulty_checker()
        self.assertEqual(result, 3)

    @patch('builtins.input', return_value='invalid')
    def test_difficulty_checker_invalid_type(self, _):
        with self.assertRaises(ValueError):
            difficulty_checker()

    @patch('builtins.input', return_value='4')
    def test_difficulty_checker_invalid_index(self, _):
        with self.assertRaises(IndexError):
            difficulty_checker()
