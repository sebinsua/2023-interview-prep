from typing import List, Tuple


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        TOTAL_LENGTH = 2 * n
        stack: List[Tuple[str, int, int]] = [("", 0, 0)]
        while stack:
            # A backtracking approach is employed here to explore all
            # possible combinations of parentheses.
            current_string, open_count, close_count = stack.pop()

            # Whenever the total number of parentheses are used
            # add the string into the `results` list.
            if open_count + close_count == TOTAL_LENGTH:
                results.append(current_string)
                continue

            # Attempt to add two items into the `stack` while ensuring the
            # resulting string remains a valid partial solution.
            #
            # (1) If we have open parentheses remaining, a string with
            #     an extra open parentheses.
            # (2) If we have a fewer close parentheses than open parentheses,
            #     a string with an extra close parentheses.
            #
            # This will cause the `stack` to exponentially quickly grow by 0 to 2 items
            # at a time but eventually it'll stop growing when the `open_count` is equal
            # to `n` and the `close_count` is equal to the `open_count`. At this point, the
            # remaining `stack` items will be processed and eventually the `while` loop
            # will exit.
            if open_count < n:
                item = (f"{current_string}(", open_count + 1, close_count)
                stack.append()

            # This is essential to ensure the strings produced are valid.
            if close_count < open_count:
                item = (f"{current_string})", open_count, close_count + 1)
                stack.append(item)

        return results
