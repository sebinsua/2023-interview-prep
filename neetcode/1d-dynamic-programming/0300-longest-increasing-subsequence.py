from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # A single character would be considered a sequence of length 1,
        # therefore, by default, at every index we will have seen a sequence
        # of length 1.
        dp = [1] * len(nums)

        # In order to build up `dp[i]`, what we need to do is to consider
        # the longest increasing subsequence of a prefix slice that we are
        # slowly growing from `1` to `len(nums)`.
        for prefix_end in range(1, len(nums)):
            # For each prefix slice, we check every index to determine
            # whether the last number of the prefix is greater than it.
            # If the last number of the prefix is greater than a number
            # in the sequence, we may be able to increase `dp[prefix_end]`.
            for i in range(prefix_end):
                # If we find a number that is less than the last number of
                # the prefix, we can look at the longest increasing subsequence
                # when this index was the `prefix_end` before and add 1 to this
                # to maximize the current `dp[prefix_end]`.
                if nums[i] < nums[prefix_end]:
                    # `dp[i]` refers to a `dp[prefix_end - n]` of an earlier
                    # iteration of the outer loop that computed the
                    # longest increasing subsequence of a prior `prefix_end`.
                    lis_at_prior_prefix_end = dp[i]

                    dp[prefix_end] = max(dp[prefix_end], lis_at_prior_prefix_end + 1)

        return max(dp)
