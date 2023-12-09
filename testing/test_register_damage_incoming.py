from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from character_actions.combat import register_damage_incoming


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_damage_incoming_damage_taken(self, mock_stdout):
        character = {'name': 'Luke Skywalker', 'hp': 5}
        enemy = {'name': 'Royal Guard', 'str': 2}
        result = register_damage_incoming(character, enemy)
        self.assertTrue(result)
        self.assertEqual(mock_stdout.getvalue().strip(), 'The enemy fought back and you took 2 damage')

    @patch('sys.stdout', new_callable=StringIO)
    def test_register_damage_incoming_character_died(self, mock_stdout):
        character = {'name': 'Luke Skywalker', 'hp': 2}
        enemy = {'name': 'Royal Guard', 'str': 50}
        result = register_damage_incoming(character, enemy)
        self.assertFalse(result)
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your HP has fallen to 0, you have died...')
