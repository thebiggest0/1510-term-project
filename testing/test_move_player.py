from unittest import TestCase
from unittest.mock import patch
import io
from character_actions.move import move_player


class TestMovePlayer(TestCase):
    def test_valid_move_right(self):
        initial_position = [1, 1]
        direction = 'd'
        map_size = 3
        game_map = [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
        actual = move_player(initial_position, direction, map_size, game_map)
        expect = [2, 1]
        self.assertEqual(actual, expect)

    def test_valid_move_left(self):
        initial_position = [1, 1]
        direction = 'a'
        map_size = 3
        game_map = [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
        actual = move_player(initial_position, direction, map_size, game_map)
        expect = [0, 1]
        self.assertEqual(actual, expect)

    def test_valid_move_up(self):
        initial_position = [1, 1]
        direction = 'w'
        map_size = 3
        game_map = [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
        actual = move_player(initial_position, direction, map_size, game_map)
        expect = [1, 0]
        self.assertEqual(actual, expect)

    def test_valid_move_down(self):
        initial_position = [1, 1]
        direction = 's'
        map_size = 3
        game_map = [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
        actual = move_player(initial_position, direction, map_size, game_map)
        expect = [1, 2]
        self.assertEqual(actual, expect)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_move(self, mock_output):
        initial_position = [0, 0]
        direction = 'w'
        map_size = 3
        game_map = [['X', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        actual = move_player(initial_position, direction, map_size, game_map)
        expect = [0, 0]
        self.assertEqual(actual, expect)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You can not go there, it is a wall\n'
        self.assertEqual(expected_output, the_game_printed_this)
