def solution(message):
    # A => 1
    # B => 2
    # C => 3
    # D => 4
    # E => 5
    # F => 6
    # G => 7
    # H => 8
    # I => 9
    # J => 10
    # K => 11
    # L => 12
    # M => 13
    # N => 14
    # O => 15
    # P => 16
    # Q => 17
    # R => 18
    # S => 19
    # T => 20
    # U => 21
    # V => 22
    # W => 23
    # X => 24
    # Y => 25
    # Z => 26
    #
    # OK, so we have patterns like these:
    # "10" => J => 1
    # "11" => AA, K => 2
    # "123" => ABC, LC, AW => 3
    # "1234" => ABCD, LCD, AWD => 3
    # "1224" => ABBD, LBD, AVD, ABX, LX => 5
    #
    # From what I can see, you have to look at characters in one element
    # or two element chunks.
    #
    # In the case, of two element chunks depending on whether `10 < num <= 26`
    # it can result in either a combination of 1 or a combination of 2.
    #
    # When the length of the message is two elements long, this is relatively
    # simple, however, if we have 3 characters or 4 characters or 5 characters
    # we have to consider these chunks at multiple places through the sequence.
    n = len(message)
    mod = int(1e9 + 7)

    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if int(message[0]) == 0 else 1

    for i in range(2, n + 1):
        # For each index, we check both the single digit and two digit number.
        # print(i, message[i-1], message[i-2:i])

        # If the single digit number is not 0, it is valid.
        if int(message[i - 1]) != 0:
            dp[i] += dp[i - 1] % mod

        # If the two digit number is between 10 and 26, it is valid.
        if 10 <= int(message[i - 2 : i]) <= 26:
            dp[i] += dp[i - 2] % mod

    return dp[-1]
