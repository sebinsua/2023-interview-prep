from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        for i in range(len(nums)):
            num ^= i
        for i in nums:
            num ^= i
        return num
