from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from character_actions.move import print_map


class TestPrintMap(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_print_map_with_player_position(self, mock_stdout):
        game_map = [
            ["J", "O"],
            ["#", "#"],
            [" ", "P"]
        ]
        player_position = [2, 1]
        expected_output = """_  _  _  _
|  J  O  |
|  #  #  |
|     P  |
-  -  -  -\n"""
        print_map(game_map, player_position)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
