def debug(matrix, dp):
    print("Matrix:")
    for row in matrix:
        print(" ".join(str(i) for i in row))

    print("\nDP values:")
    for row in dp:
        print(" ".join(str(i) for i in row))


def solution(matrix):
    if not matrix or not matrix[0]:
        return 0

    max_side = 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                # An `x` point only belongs to a larger square
                # if the top-left, top, and left points that are
                # adjacent to it are 1 values, too.
                #
                # e.g.
                #
                # 1 1
                # 1 x
                #
                # We use `min` which means that if any points contain
                # 0 there is no square to continue and we reset back
                # to 1.
                #
                # Similarly `min` ensures that we always pick the side
                # with the shortest length which is necessary if we have
                # a smaller square jutting out from a larger square and
                # don't wish to continue from its greatest side value.
                dp[i][j] = (
                    min(
                        # top-left
                        dp[i - 1][j - 1],
                        # top
                        dp[i - 1][j],
                        # left
                        dp[i][j - 1],
                    )
                    + 1
                )

                max_side = max(max_side, dp[i][j])

    debug(matrix, dp)

    return max_side * max_side
