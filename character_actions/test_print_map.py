from unittest import TestCase
from unittest.mock import patch
import io
from move import print_map


class TestPrintMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_small_map_with_player(self, mock_output):
        game_map = [['#', '_', '#'], ['_', 'X', '_'], ['#', '_', '#']]
        player_position = [1, 1]

        print_map(game_map, player_position)
        the_game_printed_this = mock_output.getvalue()

        expected_output = (
            '| # _ # |\n'
            '| _ X _ |\n'
            '| # _ # |\n'
        )
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_with_player_large_map(self, mock_output):
        game_map = [
            ['_', '_', '_', '_', '_', '_', '#', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', 'O', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
        ]
        player_position = [6, 0]
        print_map(game_map, player_position)
        the_function_printed_this = mock_output.getvalue()
        expected_output = (
            '| _ _ _ _ _ _ X _ _ _ |\n'
            '| _ _ _ _ _ _ _ O _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
            '| _ _ _ _ _ _ _ _ _ _ |\n'
        )
        self.assertEqual(expected_output, the_function_printed_this)
