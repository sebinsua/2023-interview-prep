from typing import List
from collections import Counter

# import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This is more optimal, but LeetCode has it as being less efficient:
        # counts = Counter(nums)
        # return heapq.nlargest(k, counts.keys(), counts.get)
        return [value for value, _ in Counter(nums).most_common(k)]
