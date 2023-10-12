from typing import Generator


MAX_INT32 = 2**31 - 1
MAX_SAFE_RESULT = MAX_INT32 // 10


def reverse_digits(x: int) -> Generator[int, None, None]:
    x = abs(x)
    while x != 0:
        digit = x % 10
        yield digit
        x = x // 10


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1

        result = 0
        for digit in reverse_digits(x):
            # Check for overflow before performing operation that can fail.
            if result > MAX_SAFE_RESULT:
                return 0
            result = (result * 10) + digit

        return sign * result
