def count_odd_palindromes(s: str, index: int) -> int:
    L = len(s)
    left = index - 1
    right = index + 1

    count = 0
    count += 1

    while 0 <= left < index and index <= right < L and s[left] == s[right]:
        count += 1

        left -= 1
        right += 1

    return count


def count_even_palindromes(s: str, index: int) -> int:
    L = len(s)
    left = index
    right = index + 1

    count = 0

    while 0 <= left <= index and index < right < L and s[left] == s[right]:
        count += 1

        left -= 1
        right += 1

    return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)

        count = 0
        for index in range(L):
            count += count_even_palindromes(s, index)
            count += count_odd_palindromes(s, index)

        return count
