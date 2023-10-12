class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Assuming a and b are 32-bit integers.
        x = a & 0xFFFFFFFF
        y = b & 0xFFFFFFFF
        while y != 0:
            carry = x & y
            x = (x ^ y) & 0xFFFFFFFF
            y = (carry << 1) & 0xFFFFFFFF

        # If the number is negative.
        if x & 0x80000000:
            return -((x ^ 0xFFFFFFFF) + 1)

        return x
