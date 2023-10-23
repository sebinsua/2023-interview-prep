from typing import Generator


def digits(n: int) -> Generator[int, None, None]:
    while n != 0:
        yield n % 10
        n //= 10


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while n != 1:
            # Note: you cannot use `^2` to square a number in Python
            #       as this is the XOR operator.
            n = sum([digit**2 for digit in digits(n)])
            if n in seen:
                return False
            seen.add(n)
        return True
