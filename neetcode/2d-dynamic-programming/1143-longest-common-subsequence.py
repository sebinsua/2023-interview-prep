class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        # The problem has "optimal substructure" since if you take two sequences:
        #
        # `x0, x1, x2, x3, ..., xn-1, xn`
        # `y0, y1, y2, y3, ..., yn-1, yn`
        #
        # You can recursively remove the last element of each sequence and test to see
        # whether they match:
        #
        # - If `xn == yn` the next subproblem is `x0, ..., xn-1` with `y0, ..., yn-1`.
        # - But if `xn != yn` then it is not possible to tell whether it was `xn` or `yn`
        #   which was not part of the sequence so you must consider two cases where either
        #   are removed, e.g. (1) `x0, ..., xn` with `y0, ..., yn-1`, and, (2)
        #   `x0, ..., xn-1` with `y0, ..., yn`.
        #
        # Although we know there is "optimal substructure", this only proves that the
        # problem can be solved with DFS or recursion. We only need dynamic programming
        # (e.g. top-down "memoisation" or bottom-up "tabulation") if there are
        # "overlapping subproblems". We will only know this for certain if we count
        # how often repeated subproblems come up.
        #
        # Finally, it's useful to work through a non-trivial example using tabulation:
        #
        # text1 = "xab"
        # text2 = "abxab"
        #
        # Note 1: you can work this out by hand and then fill out the matrix with
        #         longest common subsequence (LCS) values.
        # Note 2: subsequences do not need to be contiguous (although in the example
        #         I've picked this might appear to be the case).
        #
        #     -    x    a    b
        # ---------------------
        # - | 0C | 0C | 0C | 0C
        # a | 0C | 0C | 1I | 1C
        # b | 0C | 0C | 1C | 2I
        # x | 0C | 1I | 1C | 2C
        # a | 0C | 1C | 2I | 2C
        # b | 0C | 1C | 2C | 3I
        #
        # In each cell I've also added a `C` or an `I` to describe whether the cell was
        # an increment (I) from the two prefix strings with a length-1 (i-1, j-1), which
        # would be the case if there was a matching character, or, when a character does
        # not match, then a copy (C) of the longest common subsequence found so far in
        # either (i-1, j) or (i, j-1).
        #
        # Basically:
        #
        # (1) Whenever there is a match the longest common subsequence (LCS) will be
        # the LCS of the two strings that are one character shorter.
        # (2) While when there is no match, it means that we need to copy the known maximum
        # LCS so far by checking two cases: (i) using the prefix of `text1` up to and including
        # the current character and using the prefix of `text2` excluding the current character,
        # and, (ii) using the prefix of `text2` up to and including the current character and
        # using the prefix of `text1` excluding the current character. This is because when
        # characters do not match it is unknown whether either remain in the rest of the sequence.
        # A key idea behind the recurrence is that, when a character does not match another character,
        # it's not known which character is incorrect so you have to try with and without the end character
        # in each prefix string.

        # We create a 2-d `dp` matrix of `0` values.
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # We use a nested loop to iterate to granularly establish the LCS of two slices:
        # (1) the `0..i` of `text1`, and (2) the `0..j` of `text2`.
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    # When a character matches it contributes 1 to the LCS of the prefixes
                    # with lengths 1-less than the current `i` and `j`, thereby excluding
                    # the current character that we just matched.
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If the characters don't match, we have to copy across the current LCS.
                    # But to do so we need to get the maximum of two cases:
                    # 1. By including the current character from `text1` but excluding it from `text2`
                    # 2. By including the current character from `text2` but excluding it from `text1`
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # We return the LCS of the full-length `text1` with the full-length `text2`.
        return dp[len(text1)][len(text2)]
