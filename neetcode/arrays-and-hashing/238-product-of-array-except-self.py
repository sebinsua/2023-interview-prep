from typing import List
from itertools import accumulate
import operator


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = list(accumulate([1] + nums[:-1], operator.mul))
        right = list(reversed(list(accumulate([1] + nums[:0:-1], operator.mul))))

        return [l * r for l, r in zip(left, right)]
