from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price_index = 0
        max_price_index = len(prices) - 1
        max_profit = prices[max_price_index] - prices[min_price_index]

        for index, price in enumerate(prices):
            if price < prices[min_price_index]:
                min_price_index = index
                if index + 1 < len(prices):
                    max_price_index = index + 1
                    max_profit = max(
                        max_profit, prices[max_price_index] - prices[min_price_index]
                    )
            elif price > prices[max_price_index]:
                max_price_index = index
                max_profit = max(
                    max_profit, prices[max_price_index] - prices[min_price_index]
                )

        return max_profit
