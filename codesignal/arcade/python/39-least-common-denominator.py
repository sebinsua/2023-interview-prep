import functools
from math import gcd

def solution(denominators):
    return functools.reduce(
        lambda x, y: (x * y) // (gcd(x, y)),
        denominators
    )
