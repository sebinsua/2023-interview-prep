from collections import deque

def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: res[x].rotate(-x), range(n)), 0)
    return [list(d) for d in res]
