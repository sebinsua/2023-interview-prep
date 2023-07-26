from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # If we have enough operations to change all characters,
        # return the length of the string.
        if len(s) - k <= 0:
            return len(s)

        counter = defaultdict(int)
        max_length = 0

        # On every iteration we will attempt to grow the window between
        # `start_index` and `end_index`. This is the length of our sequence.
        start_index = 0
        most_common_char = s[0]
        for end_index, char in enumerate(s):
            # Increment the counter for a particular `char` and then ensure
            # that the `most_common_char` is kept in sync with the counts.
            counter[char] += 1
            most_common_char = (
                char if counter[char] > counter[most_common_char] else most_common_char
            )

            # The length of the sequence (e.g. `(end_index - start_index + 1)`)
            # increases as we iterate but if there are more than `k` gaps that need
            # to be replaced we move the `start_index` of the sequence right causing
            # it to decrease and ensuring that it's always possible to create a valid
            # sequence through `k` replacements.
            #
            # The `counter` that exists is for this sliding window (e.g. slice from
            # `start_index` to `end_index`) and must be updated if the length of the
            # window changes. We also resynchronise `most_common_char` from this if
            # the window changes size.
            if (end_index - start_index + 1) - counter[most_common_char] > k:
                original_start_char = s[start_index]

                # We slide the start of the window to the right.
                start_index += 1

                # As the `original_start_char` is no longer in the window, we
                # decrement our count of this character.
                counter[original_start_char] -= 1
                # If the `original_start_char` that we just decremented the
                # count of was the most common character, we need to recompute
                # this as it might no longer be correct.
                most_common_char = (
                    max(counter, key=counter.get)
                    if original_start_char == most_common_char
                    else most_common_char
                )

            max_length = max(max_length, end_index - start_index + 1)

        return max_length
