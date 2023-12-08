from unittest import TestCase
from unittest.mock import patch
import io
from introduction.game_start import warm_up_question


class Test(TestCase):
    @patch('builtins.input', side_effect=[6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_answer_one_try(self, mock_output, _):
        warm_up_question('Thor')
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Congratulations! Your answer is correct! Your strength increased by 5! Enjoy your game!\n'
        self.assertIn(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_answer_one_try(self, mock_output, _):
        warm_up_question('Thor')
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Sorry, wrong answer. The correct answer is 6. Enjoy your game!\n'
        self.assertIn(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=['s', 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_answer_many_tries(self, mock_output, _):
        warm_up_question('Thor')
        the_game_printed_this = mock_output.getvalue()
        expected_output_1 = 'Invalid input. Please enter a valid integer.\n'
        expected_output_2 = 'Congratulations! Your answer is correct! Your strength increased by 5! Enjoy your game!\n'
        self.assertIn(expected_output_1, the_game_printed_this)
        self.assertIn(expected_output_2, the_game_printed_this)

    @patch('builtins.input', side_effect=['!!', 2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_incorrect_answer_many_tries(self, mock_output, _):
        warm_up_question('Thor')
        the_game_printed_this = mock_output.getvalue()
        expected_output_1 = 'Invalid input. Please enter a valid integer.\n'
        expected_output_2 = 'Sorry, wrong answer. The correct answer is 6. Enjoy your game!\n'
        self.assertIn(expected_output_1, the_game_printed_this)
        self.assertIn(expected_output_2, the_game_printed_this)