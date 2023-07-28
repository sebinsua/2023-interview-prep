from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This is more optimal, but LeetCode has it as being less efficient:
        #
        # import heapq
        #
        # counts = Counter(nums)
        # return heapq.nlargest(k, counts.keys(), counts.get)

        return [value for value, _ in Counter(nums).most_common(k)]
