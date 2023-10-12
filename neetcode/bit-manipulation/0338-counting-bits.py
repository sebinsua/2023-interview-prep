from typing import List


def hamming_weight(n: int) -> int:
    count = 0
    b = 1
    while b <= n:
        if abs(n & b) == b:
            count += 1
        b *= 2
    return count


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [hamming_weight(num) for num in range(n + 1)]
