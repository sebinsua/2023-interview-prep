from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # We first count the occurrences of each character in t. This is what we'll
        # be comparing against when forming our window.
        required_counts = defaultdict(int)
        for char in t:
            required_counts[char] += 1

        # The number of unique characters in t gives us the minimum amount of unique
        # characters we need to include in our window.
        required_unique_chars = len(required_counts)

        # We'll track the number of unique characters formed in the window,
        # the current window length, and the left and right pointers.
        formed_unique_chars = 0
        window_len = float("inf")
        left, right = 0, 0

        # As we expand our window, we'll also keep track of the characters within it.
        window_counts = defaultdict(int)

        # We use the right pointer to expand the window.
        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # If the count of the current character in the window matches the desired count,
            # and it's one of the characters in `required_counts`, we have formed that character.
            if char in required_counts and window_counts[char] == required_counts[char]:
                formed_unique_chars += 1

            # Our aim is to have a window with all the required unique characters formed.
            # As long as we have that, we try to contract the window from the left,
            # to get the smallest such window.
            while left <= right and formed_unique_chars == required_unique_chars:
                char = s[left]

                # If the window we have is smaller than the previously found smallest window, update.
                if right - left + 1 < window_len:
                    window_len = right - left + 1
                    start = left

                # As we are about to move the left pointer ahead, effectively removing s[left] from the window,
                # we decrement its count in the window.
                window_counts[char] -= 1
                # If we have less of char than required now, we also reduce our formed characters.
                if (
                    char in required_counts
                    and window_counts[char] < required_counts[char]
                ):
                    formed_unique_chars -= 1

                # We can now safely shift our window to the right.
                left += 1

            # If we haven't formed all characters or if we just contracted our window,
            # we continue expanding the window.
            right += 1

        # If we found a valid window, extract it, else return an empty string.
        return "" if window_len == float("inf") else s[start : start + window_len]
