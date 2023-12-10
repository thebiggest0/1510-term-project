from unittest import TestCase
from unittest.mock import patch
from character_actions.trivia import ask_trivia
import io


class Test(TestCase):

    @patch('builtins.input', return_value='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_trivia_correct(self, mock_output, _):
        test_question = {
            "question": "Which planet does the Rebel Alliance evacuate at the start of Episode V?",
            "option_one": "Endor",
            "option_two": "Yavin IV",
            "option_three": "Alderaan",
            "option_four": "Hoth",
            "answer": 4
        }
        ask_trivia(test_question)
        actual = mock_output.getvalue()
        expected = 'Correct!'
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_trivia_question_32(self, mock_output, _):
        test_question = {
            "question": "Which planet does the Rebel Alliance evacuate at the start of Episode V?",
            "option_one": "Endor",
            "option_two": "Yavin IV",
            "option_three": "Alderaan",
            "option_four": "Hoth",
            "answer": 4
        }
        ask_trivia(test_question)
        actual = mock_output.getvalue()
        expected = 'Which planet does the Rebel Alliance evacuate at the start of Episode V?'
        self.assertIn(expected, actual)


    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_trivia_option_one(self, mock_output, _):
        test_question = {
            "question": "Which planet does the Rebel Alliance evacuate at the start of Episode V?",
            "option_one": "Endor",
            "option_two": "Yavin IV",
            "option_three": "Alderaan",
            "option_four": "Hoth",
            "answer": 4
        }
        ask_trivia(test_question)
        actual = mock_output.getvalue()
        expected = 'Endor'
        self.assertIn(expected, actual)