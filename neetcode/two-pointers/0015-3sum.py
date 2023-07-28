from typing import List
import operator


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()

        visited = set()
        for k, find in enumerate(map(operator.neg, nums)):
            if find in visited:
                continue
            visited.add(find)

            seen = {}
            for i, num in enumerate(nums):
                if i == k:
                    continue

                if find - num in seen:
                    j = seen[find - num]

                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    results.add(triplet)

                seen[num] = i

        return results
