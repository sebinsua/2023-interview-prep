from typing import List


# The key insight in solving this problem is that we don't want to find words,
# instead we want to find the "ends" of words. The boundaries of words.
# If we can do so from left-to-right, we can determine if there is an "end"
# of a word at the end of the string.
class Solution:
    def wordBreakOriginal(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)

        # It's not possible to find the words in `wordDict` in an
        # empty string.
        if L == 0:
            return False

        # We create a `dp` of `False` booleans of all of the prefixes
        # with lengths up to `L`. We also include an extra 0-length
        # so there are actually `L + 1` slots.
        #
        # We mark the `dp[0]` as `True`, even though it's not possible
        # for a string with 0-length to contain words, because what `True`
        # actually means is that we have found a valid segmentation point
        # (e.g. "word break").
        #
        # Non-intuitively `dp[prefix_end]` doesn't mean "the prefix with
        # this length contains words", but means "there is a word break
        # at `prefix_end`". It'll record every valid word break that can
        # be computed moving from left-to-right with contiguous words,
        # but, of course, the only `prefix_end` we will care about will
        # be `dp[L]`. We can consider `dp[L]` to be the following query:
        # "Is there a word-break at the length L showing that contiguous
        # words with no gaps between them can make up the prefix string
        # between 0 and L".
        dp = [False] * (L + 1)
        dp[0] = True

        for prefix_end in range(1, L + 1):
            for start in range(prefix_end):
                # We find a valid "word break" if there is a word break
                # at `dp[start]` and a word between `start` and `prefix_end`.
                if dp[start] == True and s[start:prefix_end] in wordDict:
                    dp[prefix_end] = True
                    # If we've found a valid word break, we don't
                    # need to check any further `start` indexes.
                    #
                    # This means we're always attempting to use the
                    # biggest string to fill the space between `start`
                    # and `prefix_end`.
                    #
                    # Note: There is no way for `dp[prefix_end]` to
                    #       be set to `False`.
                    break

        return dp[L]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        L = len(s)

        # It's not possible to find the words in `wordDict` in an
        # empty string.
        if L == 0:
            return False

        # `words_breaks` is a set that maintains valid word break positions.
        # We initialize with a 0 since an empty prefix (before any character)
        # is a valid word break.
        #
        # It'll record every valid word break that can be computed moving
        # from left-to-right with contiguous words, but, of course, the
        # only `prefix_end` we will care about will be `L`.
        words_breaks = {0}

        for prefix_end in range(1, L + 1):
            for start in words_breaks:
                # We find a valid "word break" if there is an exact word
                # between `start` and `prefix_end`.
                if s[start:prefix_end] in wordDict:
                    words_breaks.add(prefix_end)
                    # If we've found a valid word break, we don't
                    # need to check any further `start` indexes for
                    # that `prefix_end`.
                    #
                    # This means we're always attempting to use the
                    # biggest string to fill the space between `start`
                    # and `prefix_end`.
                    break

        # We can consider `L in word_breaks` to be the following query:
        # "Is there a word-break at the length `L` showing that contiguous
        # words with no gaps between them can make up the prefix string
        # between 0 and L".
        return L in words_breaks
