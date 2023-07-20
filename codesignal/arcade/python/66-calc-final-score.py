def solution(scores, n):
    gen = (score**2 for score in sorted(scores, reverse=True)[:n])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
