from unittest import TestCase
from move import check_valid_move


class TestCheckValidMove(TestCase):
    def test_invalid_move_to_wall(self):
        game_map = [['#', '_', '#'], ['#', 'X', '_'], ['#', '_', 'X']]
        result = check_valid_move([0, 1], game_map)
        self.assertFalse(result)

    def test_valid_move_to_empty_space(self):
        game_map = [['#', '_', '#'], ['_', 'X', '_'], ['#', '_', '#']]
        result = check_valid_move([0, 1], game_map)
        self.assertTrue(result)

    def test_valid_move_to_special_character_J(self):
        game_map = [['#', '_', '#'], ['J', 'X', '_'], ['#', '_', '#']]
        result = check_valid_move([0, 1], game_map)
        self.assertTrue(result)

    def test_valid_move_to_special_character_asterisk(self):
        game_map = [['#', '_', '#'], ['*', 'X', '_'], ['#', '_', '#']]
        result = check_valid_move([0, 1], game_map)
        self.assertTrue(result)

    def test_valid_move_to_special_character_O(self):
        game_map = [['#', '_', '#'], ['O', 'X', '_'], ['#', '_', '#']]
        result = check_valid_move([0, 1], game_map)
        self.assertTrue(result)
