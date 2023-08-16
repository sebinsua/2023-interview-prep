class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        if m == 2:
            return n
        if n == 2:
            return m

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # First I sat drawing grids for each (m, n) so I could create the mappings
        # between (m, n) and unique paths shown below:
        #
        # (0, 0) => 0
        # (0, 1) => 0
        # (1, 0) => 0
        # (1, 1) => 1
        # (1, 2) => 1
        # (1, 3) => 1
        # (1, 4) => 1
        # (1, 5) => 1
        # (2, 1) => 1
        # (2, 2) => 2
        # (2, 3) => 3
        # (2, 4) => 4
        # (2, 5) => 5
        # (2, 6) => 6
        # (2, 7) => 7
        # (3, 2) => 3
        # (3, 3) => 6
        # (3, 4) => 10
        # (3, 5) => 15
        # ...and so on...
        #
        # After doing this for a while I noticed a few patterns:
        # 1. Anything with a 0 dimension results in 0 unique paths.
        # 2. Anything with a 1 dimension results in 1 unique path.
        # 3. Anything with a 2 dimension results in the other dimension number of unique paths.
        #
        # But beyond that the sequential nature of how I had listed these relationships made it
        # practically impossible to see the recurrence relation.
        #
        # It turns out that the trick is to plot the number of unique paths in a matrix, like so:
        #
        # n\m | 0   1   2   3   4   5
        # ---------------------------
        #  0  | 0   0   0   0   0   0
        #  1  | 0   1   1   1   1   1
        #  2  | 0   1   2   3   4   5
        #  3  | 0   1   3   6  10  15
        #
        # Once the values are in a matrix/table the recurrence relation
        # is very easy to see visually, as, to compute a cell you just
        # add the cell above it to the cell to the left of it.
        #
        # dp[m][n] = dp[m - 1][n] + dp[m][n - 1]
        #
        # Plotting the unique paths in a matrix appears to be so decisive that it's basically
        # mandatory if you want to work out the recurrence relation.
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
