def solution(n):
    return [[0] * x for x in functools.reduce(lambda acc, i: [*acc, acc[i-2] + acc[i-1]], range(2, n), [0, 1])]
