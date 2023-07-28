import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = re.sub("[^a-z0-9]", "", s.lower())
        if len(formatted) <= 1:
            return True

        length = len(formatted)
        for index in range(length // 2):
            if formatted[index] != formatted[length - 1 - index]:
                return False

        return True
