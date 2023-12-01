from unittest import TestCase
from unittest.mock import patch
from game_start import name_entry


class TestNameEntry(TestCase):
    @patch('builtins.input', side_effect=['John', 'y'])
    def test_name_entry_first_try_successful(self, mock_input):
        result = name_entry()
        self.assertEqual(result, 'John')

    @patch('builtins.input', side_effect=['Alice', 'n', 'Bob', 'y'])
    def test_name_entry_try_many_times(self, mock_input):
        result = name_entry()
        self.assertEqual(result, 'Bob')

    @patch('builtins.input', side_effect=['', 'Steven', 'y'])
    def test_name_entry_with_empty(self, mock_input):
        result = name_entry()
        self.assertEqual(result, 'Steven')
