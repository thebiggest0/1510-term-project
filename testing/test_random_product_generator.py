from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import random_product_generator


class TestRandomProduct(TestCase):
    @patch('combat.random.randrange', side_effect=[-3, 7])
    def test_random_product_generator_1_negative_number(self, _):
        result = random_product_generator()
        self.assertEqual(result, ['-3 * 7 = ', -21])

    @patch('combat.random.randrange', side_effect=[-3, -7])
    def test_random_product_generator_2_negative_number(self, _):
        result = random_product_generator()
        self.assertEqual(result, ['-3 * -7 = ', 21])

    @patch('combat.random.randrange', side_effect=[12, 5])
    def test_random_product_generator_2_positive_number(self, _):
        result = random_product_generator()
        self.assertEqual(result, ['12 * 5 = ', 60])

    @patch('combat.random.randrange', side_effect=[12, 0])
    def test_random_product_generator_1_zero(self, _):
        result = random_product_generator()
        self.assertEqual(result, ['12 * 0 = ', 0])

    @patch('combat.random.randrange', side_effect=[0, 0])
    def test_random_product_generator_both_zero(self, _):
        result = random_product_generator()
        self.assertEqual(result, ['0 * 0 = ', 0])