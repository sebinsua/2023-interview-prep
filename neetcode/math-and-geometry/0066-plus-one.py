from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index >= -1:
            if index == -1:
                digits = [1] + digits
                break

            if digits[index] < 9:
                digits[index] += 1
                break

            # When a digit of 9 is found, then:
            digits[index] = 0
            index -= 1

        return digits
