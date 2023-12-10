from unittest import TestCase
from unittest.mock import patch
from character_actions.combat import random_calculate_generator
import io


class TestRandomCalculate(TestCase):
    @patch('random.randrange', side_effect=[23, 8, 2])
    def test_random_sum_generator_addition(self, _):
        result = random_calculate_generator()
        self.assertEqual(result, ['23 + (8) = ', 31])

    @patch('random.randrange', side_effect=[42, 15, 1])
    def test_random_sum_generator_subtraction(self, _):
        result = random_calculate_generator()
        self.assertEqual(result, ['42 - (15) = ', 27])
