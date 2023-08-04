def length_odd_palindrome(s: str, index: int) -> int:
    L = len(s)
    left = index
    right = index

    while 0 <= left <= index and index <= right < L and s[left] == s[right]:
        left -= 1
        right += 1

    # After the while-loop finishes `left` and `right` represent the points
    # at which the palindrome broke or was out-of-bounds, therefore we must
    # add 1 to left and -1 from right (but, we leave right alone since slices
    # are not inclusive of it otherwise).
    start = left + 1
    end = right

    return start, end


def length_even_palindrome(s: str, index: int) -> int:
    L = len(s)
    left = index
    right = index + 1

    while 0 <= left <= index and index < right < L and s[left] == s[right]:
        left -= 1
        right += 1

    start = left + 1
    end = right

    return start, end


class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)

        longest_palindrome = ""
        for index in range(L):
            start, end = length_odd_palindrome(s, index)
            if end - start > len(longest_palindrome):
                longest_palindrome = s[start:end]

            start, end = length_even_palindrome(s, index)
            if end - start > len(longest_palindrome):
                longest_palindrome = s[start:end]

        return longest_palindrome
