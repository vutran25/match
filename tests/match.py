"""
Unit tests for match module.
"""
import random
import unittest
from data.profiles import Profiles
from match.match import Match

random.seed(0)
INITIAL_ATTENDANTS = list(Profiles(100))
# Result after matching, RESULTS should be a list of tuples (male_index,female_index, score)
RESULTS = Match(INITIAL_ATTENDANTS)
PAIRS = RESULTS.pairs()


class TestMatch(unittest.TestCase):
    """
    Tests for match. Try to cover as many scenarios as possible, grouping them into different
    methods as appropriate.
    """

    def test_male_female(self):
        """
            Test if pairing is between males and females only
        """
        for couple in PAIRS:
            self.assertNotEqual(
                INITIAL_ATTENDANTS[couple[0]]["gender"], INITIAL_ATTENDANTS[couple[1]]["gender"])

    def test_50_pairs(self):
        """
            Test if there are exactly 50 pairs
        """
        self.assertEqual(len(PAIRS), 50)

    def not_repeated_person(self):
        """
            Test everyone should only pair once
        """
        for index, _ in enumerate(INITIAL_ATTENDANTS):
            count = 0
            for pair in PAIRS:
                count += pair.count(index)
            self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
