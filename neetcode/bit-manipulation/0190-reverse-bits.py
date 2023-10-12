class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        MAX = 2**31

        b = 1
        b2 = MAX
        while b <= MAX:
            if abs(n & b) == b:
                ret += b2
            b *= 2
            b2 /= 2

        return int(ret)
