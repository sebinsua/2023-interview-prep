def solution(n):
    return [
        [value for value in range(step, (step * n) + 1, step)]
        for step in range(1, n + 1)
    ]
