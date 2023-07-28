class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        seen = {}
        start_idx = 0
        max_length = 1
        for index, c in enumerate(s):
            if c in seen and seen[c] >= start_idx:
                start_idx = seen[c] + 1

            seen[c] = index
            max_length = max(max_length, index - start_idx + 1)

        return max_length
