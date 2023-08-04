from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If we wanted change for the amount 0, we can do this with 0 coins.
        if amount == 0:
            return 0

        # If we wanted change and have only a single coin, whether we can do
        # this or not depends on how many times this coin goes into the target
        # amount.
        if len(coins) == 1:
            return amount // coins[0] if amount % coins[0] == 0 else -1

        # If the minimum denomination is greater than the target amount, it will
        # not be possible to create change to make this.
        if min(coins) > amount:
            return -1

        # `dp[amount]` is the minimum number of coins required to make this amount.
        # We know that we can make the amount 0 with 0 coins, but for all other amounts
        # we start with `float('inf')`.
        #
        # The recurrence relation for this problem is:
        #
        # `dp[amount] = min(dp[amount], dp[amount - coin_denomination] + 1)`
        dp = defaultdict(lambda: float("inf"))
        dp[0] = 0
        for coin_denomination in coins:
            # We skip coin denominations that are greater than the target amount.
            if coin_denomination > amount:
                continue

            # We fill out `dp[amount]` by minimizing the number of coins against
            # this by looking at the minimum coin change for a target amount minus
            # the current coin, and then adding 1 on to represent adding this coin.
            #
            # Note: if there was never a `dp[target_amount - coin_denomination]` that
            #       resulted in a non-infinite value then the minimum will never
            #       be updated with a value and the program will eventually return `-1`.
            #
            #       The approach works because `target_amount - coin_denomination == 0`
            #       at some point and so on, and `dp` gets filled up.
            for target_amount in range(coin_denomination, amount + 1):
                # This is reminiscent of two-sum which also looked back at previous values
                # in this way.
                min_change_to_make_previous_target = dp[
                    target_amount - coin_denomination
                ]
                dp[target_amount] = min(
                    dp[target_amount], min_change_to_make_previous_target + 1
                )

        return dp[amount] if dp[amount] != float("inf") else -1
