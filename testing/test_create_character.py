from unittest import TestCase
from character.character import create_character


class TestCreateCharacter(TestCase):
    def test_creat_character_case_1(self):
        name = 'Thor'
        actual = create_character(name)
        expected = {
            'name': 'Thor',
            'level': 1,
            'experience': 0,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        self.assertEqual(actual, expected)

    def test_creat_character_case_2(self):
        name = 'Loki'
        actual = create_character(name)
        expected = {
            'name': 'Loki',
            'level': 1,
            'experience': 0,
            'hp': 50,
            'str': 15,
            'int': 15,
            'x-coordinate': 0,
            "y-coordinate": 0
        }
        self.assertEqual(actual, expected)