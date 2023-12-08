from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import random_enemy


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
