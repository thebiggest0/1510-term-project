from unittest import TestCase
from unittest.mock import patch
from character_actions.trivia import player_choice


class Test(TestCase):

    @patch('builtins.input', return_value='1')
    def test_ask_trivia_answer_one(self, _):
        actual = player_choice()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', return_value='2')
    def test_ask_trivia_answer_two(self, _):
        actual = player_choice()
        expected = 2
        self.assertEqual(actual, expected)
