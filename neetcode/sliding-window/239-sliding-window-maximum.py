from typing import List
from collections import deque


class Solution:
    # I originally attempted to solve this question by negating the values within
    # a `heapq` to create a max-heap and keeping this in sync with a `deque` of the
    # values within the window, however, sometimes removing a value from the front
    # of the window resulted in needing to remove a value from the middle of the
    # max-heap and this was computationally expensive as it would generally involve
    # recreating the heap.
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        # 1. We use a `deque` as we want to be able to cheaply get the maximum value from
        #    the front of the list.
        # 2. We store indices because we need to be able to determine whether a value has
        #    left the `k` window range and this isn't possible if we'd stored the value.
        indices = deque()
        for i, num in enumerate(nums):
            # Remove the left-most index (which points to the max value) when it goes out
            # of the window range.
            if len(indices) > 0 and indices[0] < i - k + 1:
                indices.popleft()

            # Moving from right-to-left remove all indices that point towards numbers that
            # are less than the new number and then add the new number to the end of the deque.
            #
            # If we get a new max value it will result in a one-element deque.
            #
            # For example (ignoring the removal of the left-most element shown above):
            #
            # 1. If the `indices` pointed to numbers like `[5, 4, 2, 1]` and the new number
            #    is `9`, the new `indices` will only point to `[9]`.
            # 2. If the `indices` pointed to numbers like `[12, 11, 8, 3, 4]` and the new
            #    number is `9`, the new `indices` will point to `[12, 11, 9]`
            # 3. If the `indices` pointed to `[38, 10, 14]` and the new number is `9`, the new
            #    `indices` will point to `[38, 10, 14, 9]`
            while len(indices) > 0 and nums[indices[-1]] < num:
                indices.pop()
            indices.append(i)

            # The front element of the `indices` deque will always point to the maximum value
            # of the window, while the remaining indices are pointers to candidate maximum values
            # that we've seen before. The reason that they are only candidates is that it's possible
            # that these indices are no longer within the window range and might be removed, and
            # because it's possible that a future iteration will see a larger value causing any
            # of the indices pointing to a value below this to be removed.

            # In the first 0..k iterations we've not seen a window large enough to know the maximum
            # value of the first window of k-length.
            if i < k - 1:
                continue

            # Once we've seen a full window range of k-elements we can begin to append the current
            # maximum value to the result list on every iteration.
            result.append(nums[indices[0]])

        return result
