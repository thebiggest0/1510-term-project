from unittest import TestCase
import io
from unittest.mock import patch
from game_start import select_difficulty


class Test(TestCase):
    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_difficulty_easy(self, mock_stdout, _):
        result = select_difficulty()
        self.assertEqual(result, 1)
        expected_output = (
            'Please select the difficulty of the game:\n'
            'Easy: For beginners, enemies will have lower HP and do less damage.\n'
            'Medium: For casuals, enemies will have higher HP and do more damage.\n'
            'Hard: For experts, enemies will be----- classified data.\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_difficulty_medium(self, mock_stdout, _):
        result = select_difficulty()
        self.assertEqual(result, 2)
        expected_output = (
            'Please select the difficulty of the game:\n'
            'Easy: For beginners, enemies will have lower HP and do less damage.\n'
            'Medium: For casuals, enemies will have higher HP and do more damage.\n'
            'Hard: For experts, enemies will be----- classified data.\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_difficulty_hard(self, mock_stdout, _):
        result = select_difficulty()
        self.assertEqual(result, 3)
        expected_output = (
            'Please select the difficulty of the game:\n'
            'Easy: For beginners, enemies will have lower HP and do less damage.\n'
            'Medium: For casuals, enemies will have higher HP and do more damage.\n'
            'Hard: For experts, enemies will be----- classified data.\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['?', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_difficulty_try_twice_easy(self, mock_stdout, _):
        result = select_difficulty()
        self.assertEqual(result, 1)
        expected_output = (
            'Please select the difficulty of the game:\n'
            'Easy: For beginners, enemies will have lower HP and do less damage.\n'
            'Medium: For casuals, enemies will have higher HP and do more damage.\n'
            'Hard: For experts, enemies will be----- classified data.\n'
            'Invalid input! You must input an integer between 1-3 inclusive.\n'
            'Please select the difficulty of the game:\n'
            'Easy: For beginners, enemies will have lower HP and do less damage.\n'
            'Medium: For casuals, enemies will have higher HP and do more damage.\n'
            'Hard: For experts, enemies will be----- classified data.\n'
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)