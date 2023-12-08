from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import attack_lightsaber


class TestAttackLightsaber(TestCase):
    @patch('builtins.input', side_effect=['6'])
    @patch('combat.random_calculate_generator', return_value=('What is 7 + 3? ', 10))
    def test_attack_lightsaber_incorrect_answer(self, _, __):
        character_data = {'name': 'Jedi Knight', 'str': 5, 'health': 100, 'attack': 25, 'defense': 15}
        result = attack_lightsaber(character_data)
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['10'])
    @patch('combat.random_calculate_generator', return_value=('What is 5 * 2? ', 10))
    def test_attack_lightsaber_correct_answer(self, _, __):
        character_data = {'name': 'Jedi Knight', 'str': 5, 'health': 100, 'attack': 25, 'defense': 15}
        result = attack_lightsaber(character_data)
        self.assertEqual(result, 6)

    @patch('builtins.input', side_effect=['abc'])
    def test_attack_lightsaber_invalid_answer(self, _):
        character_data = {'name': 'Jedi Knight', 'str': 5, 'health': 100, 'attack': 25, 'defense': 15}
        result = attack_lightsaber(character_data)
        self.assertEqual(result, 1)
