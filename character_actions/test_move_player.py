from unittest import TestCase
from unittest.mock import patch
from move import move_player


class TestMovePlayer(TestCase):
    def test_valid_move_right(self):
        initial_position = [1, 1]
        result = move_player(initial_position, 'd', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [2, 1])

    def test_valid_move_left(self):
        initial_position = [1, 1]
        result = move_player(initial_position, 'a', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [0, 1])

    def test_valid_move_up(self):
        initial_position = [1, 1]
        result = move_player(initial_position, 'w', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [1, 0])

    def test_valid_move_down(self):
        initial_position = [1, 1]
        result = move_player(initial_position, 's', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [1, 2])

    def test_invalid_move_wall(self):
        initial_position = [1, 1]
        result = move_player(initial_position, 'a', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [1, 1])

    def test_invalid_move_out_of_bounds(self):
        initial_position = [0, 0]
        result = move_player(initial_position, 'a', 3, [['#', '#', '#'], ['#', ' ', '#'], ['#', '#', '#']])
        self.assertEqual(result, [0, 0])
