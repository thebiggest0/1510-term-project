from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from combat import register_damage_outgoing


class TestDamageOut(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_register_damage_outgoing_damage_dealt(self, mock_stdout):
        enemy_data = {"name": "Royal Guard", "hp": 50}
        result = register_damage_outgoing(enemy_data, 30)
        self.assertFalse(result)
        self.assertEqual(mock_stdout.getvalue(), 'You dealt 30 to Royal Guard\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_register_damage_outgoing_enemy_slay(self, mock_stdout):
        enemy_data = {"name": "Royal Guard", "hp": -10}
        result = register_damage_outgoing(enemy_data, 80)
        self.assertTrue(result)
        self.assertEqual(mock_stdout.getvalue(), 'You slain Royal Guard\n')
