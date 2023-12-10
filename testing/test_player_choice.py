from unittest import TestCase
from unittest.mock import patch
from character_actions.trivia import player_choice
import io


class Test(TestCase):

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_trivia_answer_one(self, mock_output, _):
        actual = player_choice()
        the_game_printed_this = mock_output.getvalue()
        expected = 1
        expected_output = 'The force ghost asks you to choose between stats or health\n'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_trivia_answer_two(self, mock_output, _):
        actual = player_choice()
        the_game_printed_this = mock_output.getvalue()
        expected = 2
        expected_output = 'The force ghost asks you to choose between stats or health\n'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)
