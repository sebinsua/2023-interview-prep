def solution(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    # An empty block can only be filled once. Something something combinatronics.
    dp[0] = 1
    # 4x1 can only be filled once.
    dp[1] = 1
    # 4x2 can be filled in 5 ways.
    # - VVVV
    # - VVHH
    # - HHVV
    # - VVHH
    # - VHHV
    dp[2] = 5
    for i in range(3, n + 1):
        # I couldn't work this one out on my own...
        # See: https://math.stackexchange.com/questions/664113/count-the-ways-to-fill-a-4-times-n-board-with-dominoes
        dp[i] = dp[i - 1] + 5 * dp[i - 2] + dp[i - 3] - dp[i - 4]

        # I guess in an interview situation my best option would be
        # to bruteforce this by generating all combinations...?

    return dp[n]
