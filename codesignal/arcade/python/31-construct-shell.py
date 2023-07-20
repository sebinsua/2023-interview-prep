def solution(n):
    return [
        [0] * (i + 1 if i + 1 <= n else 2 * n - 1 - i)
        for i in range(2 * n - 1)
    ]
