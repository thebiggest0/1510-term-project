from unittest import TestCase
from character_actions.trivia import star_wars_trivia
from unittest.mock import patch


class TestStarWarsTrivia(TestCase):

    @patch('random.randrange', return_value=1)
    def test_trivia_question_one(self, _):

        expected = star_wars_trivia()
        actual = {
            "question": "What is the title of Episode III?",
            "option_one": "The Phantom Menace",
            "option_two": "Attack of the Clones",
            "option_three": "Revenge of the Sith",
            "option_four": "A New Hope",
            "answer": 3
        }
        self.assertEqual(expected, actual)

    @patch('random.randrange', return_value=35)
    def test_trivia_question_thirty_five(self, _):

        expected = star_wars_trivia()
        actual = {
            "question": "Who is Leia's adoptive father?",
            "option_one": "Mon Mothma",
            "option_two": "Garm Bel Iblis",
            "option_three": "Owen Lars",
            "option_four": "Bail Organa",
            "answer": 4
        }
        self.assertEqual(expected, actual)
