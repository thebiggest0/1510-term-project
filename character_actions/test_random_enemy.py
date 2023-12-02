from unittest import TestCase
from unittest.mock import patch
from combat import random_enemy


class TestRandomEnemy(TestCase):

    @patch('random.randrange', side_effect=[4, 3])
    def test_random_enemy_level_4(self, _):
        expected = {
                    'name': 'Sith Troopers',
                    'difficulty': 2,
                    'hp': 50,
                    'str': 10,
                    'experience': 5}
        actual = random_enemy()
        self.assertEqual(expected, actual)

    @patch('random.randrange', side_effect=[3, 0])
    def test_random_enemy_level_not_4(self, _):
        expected = {
                    "name": "Clone Trooper",
                    "difficulty": 1,
                    "hp": 20,
                    "str": 2,
                    "experience": 2
                }
        actual = random_enemy()
        self.assertEqual(expected, actual)

    @patch('combat.save_data.read_enemy')
    @patch('combat.random.randrange')
    def test_random_enemy_level_other(self, mock_randrange, mock_read_enemy):
        mock_randrange.return_value = 2
        mock_read_enemy.return_value = {
            'Clone Trooper': {'name': 'Clone Trooper', 'health': 100, 'attack': 20, 'defense': 10},
            'Battle Droids': {'name': 'Battle Droids', 'health': 80, 'attack': 15, 'defense': 8},
            'Tusken Raiders': {'name': 'Tusken Raiders', 'health': 90, 'attack': 18, 'defense': 12}
        }

        result = random_enemy()

        self.assertIn(result['name'], ['Clone Trooper', 'Battle Droids', 'Tusken Raiders'])
        self.assertEqual(set(result.keys()), {'name', 'health', 'attack', 'defense'})
