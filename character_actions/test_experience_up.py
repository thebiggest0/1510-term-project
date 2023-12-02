from unittest import TestCase
from combat import experience_up


class TestExperienceUp(TestCase):
    def test_experience_up_case_1(self):
        character = {'name': 'Luke Skywalker', 'experience': 50}
        enemy = {'name': 'Royal Guard', 'experience': 50}
        experience_up(character, enemy)
        actual = character['experience']
        expected = 100
        self.assertEqual(actual, expected)

    def test_experience_up_case_2(self):
        character = {'name': 'Yoda', 'experience': 150}
        enemy = {'name': 'Bounty Hunters', 'experience': 20}
        experience_up(character, enemy)
        actual = character['experience']
        expected = 170
        self.assertEqual(actual, expected)

    def test_experience_up_case_3(self):
        character = {'name': 'Han Solo', 'experience': 10}
        enemy = {'name': 'Mandalorian', 'experience': 200}
        experience_up(character, enemy)
        actual = character['experience']
        expected = 210
        self.assertEqual(actual, expected)
