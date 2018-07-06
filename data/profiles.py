"""
Profiles for matching.
"""
import random


class Profiles(object):
    """
    Factory for creating profiles.
    """

    def __init__(self, count):
        """
        Generate profiles in pairs.
            - count: Must be an even number so we get equal number of men and women.
        """
        assert count % 2 == 0

        self.count = count
        self.index = 0
        self.balance = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            self.index += 1

            # Balance out males and females
            if self.count - self.index < abs(self.balance):
                gender = self.balance < 0
            else:
                gender = random.random() > 0.5
            self.balance += 1 if gender else -1

            return {
                "gender": gender,
                "country": (random.randint(0, 2), random.random()),
                "diet": (random.randint(0, 2), random.random()),
                "drinking": (random.random() > 0.5, random.random()),
                "language": (random.randint(0, 3), random.random()),
                "religion": (random.randint(0, 3), random.random()),
                "smoking": (random.random() > 0.5, random.random())
            }
        else:
            self.index = 0
            raise StopIteration

    def next(self):
        """
        Next application, randomly generated.
        """
        return self.__next__()
