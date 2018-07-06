"""
Invoking the matches.
"""


import random
from data.profiles import Profiles
from match.match import Match


class Run(object):
    """
    Run the matches.
    """

    def print_pairings(self):
        """
        Print out the pairings for first date, along with the combined scores.
        """
        random.seed(0)
        everyone = Match(Profiles(100))
        pairs_list = everyone.pairs()
        for index, (male, female, score) in enumerate(pairs_list):
            print("{:2}: {:2} vs {:2} with the score {:.3f}".format(
                index + 1, male + 1, female + 1, score))


if __name__ == "__main__":
    Run().print_pairings()
