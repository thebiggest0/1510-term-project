from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import combat_selection


class TestCombatSelect(TestCase):
    @patch('combat.attack_lightsaber', return_value=1)
    def test_combat_selection_attack_lightsaber(self, mock_attack_lightsaber):
        user_choice = 1
        character_data = {'name': 'Jedi Knight', 'health': 100, 'attack': 25, 'defense': 15}
        result = combat_selection(user_choice, character_data)
        self.assertEqual(result, 1)
        mock_attack_lightsaber.assert_called_with(character_data)

    @patch('combat.attack_force', return_value=2)
    def test_combat_selection_attack_force(self, mock_attack_force):
        user_choice = 2
        character_data = {'name': 'Jedi Knight', 'health': 100, 'attack': 25, 'defense': 15}
        result = combat_selection(user_choice, character_data)
        self.assertEqual(result, 2)
        mock_attack_force.assert_called_with(character_data)

    @patch('combat.run_away', return_value=-1)
    def test_combat_selection_run_away(self, mock_run_away):
        user_choice = 3
        character_data = {'name': 'Jedi Knight', 'health': 100, 'attack': 25, 'defense': 15}
        result = combat_selection(user_choice, character_data)
        self.assertEqual(result, -1)
        mock_run_away.assert_called_once()
