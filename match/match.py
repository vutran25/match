"""
Match making.
"""


class Match(object):
    """
    Find matches.
    """

    def __init__(self, profiles):
        self.profiles = profiles

    def __score_for_a_pair(self, person1, person2):
        """
        Calculating the likable score from person1 to person2
            -person1: a dictionary representing a male or female
            -person2: a dictionary representing a female or male
        """
        score = 0
        for key, value in person1.items():
            # ignore the "gender" key because we don't need to compare gender
            if key != "gender":
                if value[0] == person2[key][0]:
                    score += (value[1] + person2[key][1])
                else:
                    score -= (value[1] + person2[key][1])
        return score

    def pairs(self):
        """
        Find pairings for first date.
        """
        males, females, selected_pair_with_score, selected_people = [], [], [], []
        profiles_list = list(self.profiles)
        # Separate into male and female list with its original index
        for profile in profiles_list:
            if profile["gender"]:
                males.append((profile, profiles_list.index(profile)))
            else:
                females.append((profile, profiles_list.index(profile)))
        pairs_with_scores = []
        # Calculate the score for every pairs
        for male in males:
            for female in females:
                score = self.__score_for_a_pair(
                    male[0], female[0])
                pairs_with_scores.append(
                    (male[1], female[1], score))
        # Sort all pairs by score from highest to lowest
        pairs_with_scores.sort(key=lambda t: t[2], reverse=True)
        # Filter out the perfect couple for everyone
        for score in pairs_with_scores:
            if score[0] not in selected_people and score[1] not in selected_people:
                selected_people.append(score[0])
                selected_people.append(score[1])
                selected_pair_with_score.append(score)
        # selected_pair_with_score is a tuple
        # with 3 elements inside(male_index,female_index,score) index base 0
        return selected_pair_with_score
