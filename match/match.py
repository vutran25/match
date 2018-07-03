"""
Match making.
"""


class Match(object):
    """
    Find matches.
    """

    def __init__(self, profiles):
        self.profiles = profiles

    def pairs(self):
        """
        Find pairings for first date.
        """
