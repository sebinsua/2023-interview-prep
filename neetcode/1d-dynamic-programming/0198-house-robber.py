from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # e.g.
        # [1, 10, 8, 87, 100]
        # In this case there are 5 items.
        # The result we expect is 100.
        #
        # Recurrence relation is: max(dp[i - 1], dp[i - 2] + nums[i])
        #
        # f([]) => 0 = 0
        # f([1]) => n[0] = 1
        # f([1, 10]) => max(n[0], n[1]) = 10
        # f([1, 10, 8]) => max(f([1, 10]), f([1]) + nums[2]) = 10
        # f([1, 10, 8, 87]) => max(f([1, 10, 8]), f([1, 10]) + nums[3]) = 97
        # f([1, 10, 8, 87, 100]) => max(f([1, 10, 8, 87]), f([1, 10, 8]) + nums[4]) = 110
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # We setup a dynamic array containing a sliding maximum value,
        # and we make the start value within `dp[0]` be `nums[0]`.
        # If there are two items we get the `max()` of these and
        # place that within `dp[1]`.
        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
