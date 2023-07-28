from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # In order to check whether there is a permutation of `s1` within `s2`
        # we use a sliding window approach and check whether the count of characters
        # within `s1` is found within `s2` when moving the window from left-to-right.
        #
        # Key insights:
        # 1. A permutation is a string with the same count of characters.
        # 2. We can use a fixed window size as permutations are strings of the same length.
        window_size = len(s1)

        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:window_size])

        if s1_counts == s2_counts:
            return True

        for i in range(window_size, len(s2)):
            leftmost_character_to_remove = s2[i - window_size]
            new_rightmost_character_to_add = s2[i]

            s2_counts[leftmost_character_to_remove] -= 1
            s2_counts[new_rightmost_character_to_add] += 1

            if s1_counts == s2_counts:
                return True

        return False
