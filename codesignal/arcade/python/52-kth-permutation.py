from itertools import permutations, islice

def solution(numbers, k):
    return next(islice(sorted(permutations(numbers)), k - 1, k))
