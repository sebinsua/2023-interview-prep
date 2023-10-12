from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = nums[0]
        for index in range(1, len(nums)):
            single_number ^= nums[index]

        return single_number
