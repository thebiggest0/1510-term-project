from unittest import TestCase
from unittest.mock import patch
import io
from character_status import level_up


class TestLevelUp(TestCase):
    def test_level_1_unchanged(self):
        character_info = {
            'name': 'Thor',
            'level': 1,
            'experience': 10,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        actual = level_up(character_info)
        expected = {
            'name': 'Thor',
            'level': 1,
            'experience': 10,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        self.assertEqual(actual, expected)

    def test_level_2_unchanged(self):
        character_info = {
            'name': 'Thor',
            'level': 2,
            'experience': 110,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        actual = level_up(character_info)
        expected = {
            'name': 'Thor',
            'level': 2,
            'experience': 110,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_1_level_up_to_2(self, mock_output):
        character_info = {
            'name': 'Thor',
            'level': 1,
            'experience': 110,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        actual = level_up(character_info)
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
        expected_output = 'Congratulations Thor! you\'ve leveled up!'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_2_level_up_to_3(self, mock_output):
        character_info = {
            'name': 'Thor',
            'level': 2,
            'experience': 210,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        actual = level_up(character_info)
        expected = {
            'name': 'Thor',
            'level': 3,
            'experience': 10,
            'hp': 60,
            'str': 16,
            'int': 16,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Congratulations Thor! you\'ve leveled up!'
        self.assertEqual(actual, expected)
        self.assertIn(expected_output, the_game_printed_this)
