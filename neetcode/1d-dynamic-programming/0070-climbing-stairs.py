class Solution:
    def climbStairs(self, n: int) -> int:
        # The sequences are like so:
        #
        # f(1) => 1
        # 1
        # f(2) => 2
        # 1, 1; 2
        # f(3) => 3
        # 1, 1, 1; 2, 1; 1, 2
        # f(4) => 5
        # 1, 1, 1, 1; 2, 2; 2, 1, 1; 1, 1, 2; 1, 2, 1
        # f(5) => 8
        # 1, 1, 1, 1, 1; 2, 2, 1; 2, 1, 2; 1, 2, 2; 1, 1, 1, 2;  1, 1, 2, 1; 1, 2, 1, 1; 2, 1, 1, 1
        #
        # This is actually the fibonacci sequence.
        # The recurrence relation for `f(n)` is `f(n) = f(n - 1) + f(n - 2)`.
        i = 1
        a, b = 1, 1
        while i < n:
            a, b = b, a + b
            i += 1
        return b
