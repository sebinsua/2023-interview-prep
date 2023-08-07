from typing import List


class Solution:
    def maxProductOriginal(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums[0] * nums[1], *nums[:2])

        max_dp = [0] * L
        min_dp = [0] * L

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for n in range(1, L):
            values = [max_dp[n - 1] * nums[n], min_dp[n - 1] * nums[n], nums[n]]
            max_dp[n] = max(*values)
            min_dp[n] = min(*values)

        return max(max_dp)

    def maxProduct(self, nums: List[int]) -> int:
        # Normally problems like this can be solved with an approach
        # like two-pointers but the existence of negative numbers
        # in the sub-array means it's possible for it to flip from
        # being a large negative number to a large positive number
        # or vice versa when a negative number occurs in the sequence.
        #
        # DFS would also suffer from the same problem since we'd not be
        # able to prune the search space due to not knowing if a negative
        # number might become a large positive number at the end.
        # DFS would also be problematic in general due to the possibility
        # that a sequence could be front-loaded with low numbers and
        # finally could have a large number at the end making a sub-array
        # have its maximum product. You wouldn't be able to avoid testing
        # every sub-array up to this point.
        #
        # This suggests that we'll need to use a dynamic programming
        # approach to optimally solve this problem.
        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums[0] * nums[1], *nums[:2])

        # We create a `dp[i]` for both the highest positive
        # value and highest negative value up to a particular
        # index `i`. By default, if there is no positive number
        # or negative number, we can expect `dp[i]` to be 0.
        #
        # The reason we need a `positive_dp` and `negative_dp`
        # is that if we have a negative number then it only
        # produces a maximum value if it is multiplied by
        # a negative number and vice versa.
        positive_dp = [0] * L
        negative_dp = [0] * L
        positive_dp[0] = max(nums[0], 0)
        negative_dp[0] = min(nums[0], 0)

        for i in range(1, L):
            # If the current value is 0, then we skip it, since both
            # `positive_dp` and `negative_dp` will be 0.
            if nums[i] == 0:
                continue

            # Depending on whether the current value is greater than 0
            # or less than 0, we update `positive_dp` or `negative_dp`
            # in different ways.
            #
            # We always ensure that `positive_dp` has the maximum positive
            # value we can achieve added into it, while `negative_dp` has
            # the maximum negative value we can achieve added into it.
            # This is done by always multiplying by the correct previous
            # number, and, if that is 0, producing either the number itself
            # (in the case of the current value being positive), or producing
            # 0 (in the case of the current number being negative).
            if nums[i] > 0:
                positive_dp[i] = (
                    positive_dp[i - 1] * nums[i] if positive_dp[i - 1] != 0 else nums[i]
                )
                negative_dp[i] = (
                    negative_dp[i - 1] * nums[i] if negative_dp[i - 1] != 0 else 0
                )
            else:
                positive_dp[i] = (
                    negative_dp[i - 1] * nums[i] if negative_dp[i - 1] != 0 else 0
                )
                negative_dp[i] = (
                    positive_dp[i - 1] * nums[i] if positive_dp[i - 1] != 0 else nums[i]
                )

        return max(positive_dp)
