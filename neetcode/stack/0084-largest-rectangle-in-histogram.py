from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # There are two phases of this algorithm.
        #
        # - The first phase calculates the areas of rectangles that are
        #   terminated by a shorter height.
        # - The second phase calculates the areas of rectangles that were
        #   not interrupted by any shorter heights and therefore can extend
        #   to the very end of the histogram. While this phase operates on
        #   any leftover heights, the canonical example is a sequence of
        #   ascending heights that have not been interrupted by a shorter one.
        max_area = 0

        # The stack will keep track of potential starting points of rectangles:
        #
        # e.g. (start_index, height)
        #
        # Each stack item contains a `start_index` and a valid height
        # that could be reached at this index.
        #
        # The height isn't the height at that index. It's the height
        # which can be maintained from that index as an unbroken
        # rectangle up to the last iteration's index.
        #
        # It will be maintained in a way that ensures that:
        # (1) Elements are stored in ascending order of this height.
        # (2) It represents the beginning of a rectangle that could potentially
        #     extend to be the largest rectangle of that height.
        stack = []

        # For each height:
        for index, height in enumerate(heights):
            start_index = index

            # We traverse backwards through the stack, popping
            # previous heights that are taller than the current
            # height and using each of these as the start point
            # of a new rectangle.
            while stack and stack[-1][1] > height:
                previous_index, previous_height = stack.pop()

                # For each rectangle we calculate its area by extending
                # from their `start_index` to the current index.
                rectangle_area = previous_height * (index - previous_index)
                max_area = max(max_area, rectangle_area)

                start_index = previous_index

            # At this point the `start_index` is either the index of the current
            # height, if there were no items in the stack that were taller than
            # this, or if there were items in the stack that were taller than this
            # then it might be the last item that was taller during the backwards
            # traversal.
            #
            # We stopped traversing backwards through the stack when we encountered
            # a height that was less than the current height, as we need to add
            # `(start_index, height)` items into the stack which we can start future
            # rectangles from, and these are only valid if you can reach that height
            # at the associated `start_index`.
            stack.append((start_index, height))

        # If a height is still in the stack at the end, that means it has not
        # been "interrupted" by any shorter heights and it can be extended to the
        # end of the histogram to calculate its area.
        last_height_index = len(heights) - 1
        for index, height in stack:
            # We add one as the area of the rectangle should be inclusive of
            # the last height.
            rectangle_area = height * ((last_height_index - index) + 1)
            max_area = max(max_area, rectangle_area)

        return max_area
