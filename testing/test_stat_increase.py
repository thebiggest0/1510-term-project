from unittest import TestCase
from unittest.mock import patch
import io
from character.character import stat_increase


class TestStatIncrease(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stat_increase_case_1(self, mock_output):
        character_info = {
            'name': 'Thor',
            'level': 2,
            'experience': 10,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        stat_increase(character_info)
        actual = character_info
        expected = {
            'name': 'Thor',
            'level': 2,
            'experience': 10,
            'hp': 60,
            'str': 16,
            'int': 16,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Your stats have increased!'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stat_increase_case_2(self, mock_output):
        character_info = {
            'name': 'Thor',
            'level': 3,
            'experience': 10,
            'hp': 100,
            'str': 10,
            'int': 10,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        stat_increase(character_info)
        actual = character_info
        expected = {
            'name': 'Thor',
            'level': 3,
            'experience': 10,
            'hp': 120,
            'str': 11,
            'int': 11,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Your stats have increased!'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)