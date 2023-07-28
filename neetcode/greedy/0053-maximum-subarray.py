from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We special-case empty inputs and one-element inputs.
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        max_sum = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            # This is an implementation of Kadane's algorithm.
            # We restart the sum whenever the value of the sum
            # goes below 0 (by restarting at num), and whenever
            # the sum is greater than other seen so far, we 
            # record it.
            current_sum = max(current_sum, 0) + num
            max_sum = max(max_sum, current_sum)
        
        return max_sum