from functools import cache


@cache
def solution_recursive(n):
    # 1 = 1                                                                   (1)
    # 2 = 1 1, 2                                                              (2)
    # 3 = 1 2, 2 1, 1 1 1                                                     (3)
    # 4 = 2 2, 1 1 2, 2 1 1, 1 2 1, 1 1 1 1                                   (5)
    # 5 = 1 2 2, 2 1 2, 2 2 1, 1 1 1 2, 1 1 2 1, 1 2 1 1, 2 1 1 1, 1 1 1 1 1  (8)
    if n == 1:
        return 1
    if n == 2:
        return 2

    return solution(n - 1) + solution(n - 2)


def solution(n):
    # 1 = 1                                                                   (1)
    # 2 = 1 1, 2                                                              (2)
    # 3 = 1 2, 2 1, 1 1 1                                                     (3)
    # 4 = 2 2, 1 1 2, 2 1 1, 1 2 1, 1 1 1 1                                   (5)
    # 5 = 1 2 2, 2 1 2, 2 2 1, 1 1 1 2, 1 1 2 1, 1 2 1 1, 2 1 1 1, 1 1 1 1 1  (8)
    dp = [1, 1, 2] + [-1] * (n - 2)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
