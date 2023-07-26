from typing import List
from itertools import takewhile, count


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The longest consecutive sequence is 0 if the
        # length of the array is 0.
        if len(nums) == 0:
            return 0

        longest = 0

        # But otherwise we will calculate it by creating
        # a lookup set and looping through the unique items
        # in this.
        seen = set(nums)
        for num in seen:
            # We skip any numbers that are not the first of their
            # requisite sequence by detecting if there is a number
            # before them and if so skipping to the next iteration.
            if num - 1 in seen:
                continue

            # We count up from the num while this value is in the `seen` set,
            # and sum a `1` value for each of these to get the length of a
            # sequence.
            length = sum(
                1 for _ in takewhile(lambda find: find in seen, count(start=num))
            )

            # We then check to see if this sequence is the longest seen so far,
            # and if so update `longest`.
            longest = max(longest, length)

        return longest
