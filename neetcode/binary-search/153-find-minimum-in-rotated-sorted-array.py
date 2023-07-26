from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Special case for lists with only two elements.
        if len(nums) == 2:
            return min(*nums)

        # As the array has been sorted and then rotated, it's not actually correctly
        # sorted and we can't use a binary search in the conventional way. However,
        # because we're able to make definitive decisions on which side the minimum
        # value will be found at on every iteration we're still able to use binary
        # search, if we make our comparison about which side is sorted/unsorted.
        #
        # Key points on the overall algorithm:
        # 1. The rotation point is the minimum value.
        # 2. The key idea is to identify which half of the array the rotation point lies in.
        # 3. On every iteration there will be two sides: one sorted and another unsorted.
        # 4. The rotation point will be found within the side that is unsorted.
        #
        # Example: [6, 7, 1, 2, 3, 4, 5]
        # Left-side (6, 7, 1), Mid Point (2), Right-side (3, 4, 5)
        # Rotation point (1) found within the left-side!
        #
        # Example: [3, 4, 5, 6, 7, 1, 2]
        # Left-side (3, 4, 5), Mid Point (6), Right-side (7, 1, 2)
        # Rotation point (1) found within the right-side!
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left) // 2)

            # Key points on the comparison:
            # 1. Because the elements in the list of numbers are unique, there is no difference
            #    between `>` and `>=` comparisons.
            # 2. Normally when doing a binary search we know the target value or are trying to
            #    minimize a value below some kind of threshold, however in this case there is no
            #    target and what we are trying to do is to find the minimum value.
            #    We know that the minimum value is the 'rotation point', so what we are attempting
            #    to do is to select the side which contains this and move to it. A side contains
            #    the rotation point if its left-most element is greater than its right-most element,
            #    as this means that in some sense the numbers are out-of-sequence.
            #
            #    For example, if `nums[mid] > nums[right]` or `nums[left] > nums[mid]` we know that
            #    the rotation point is found within either the right-side or left-side respectively.
            #
            #    Therefore, we compare the mid-element to the right-most element. If it is greater
            #    that implies the rotation has happened on the right-side so we move `left` to `mid + 1`.
            #    Otherwise, the rotation is either in the left-side or the midpoint itself, and we
            #    need to move to the left-side, so we move `right` to `mid`.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # When 'left' and 'right' converge we've found the smallest number.
        return nums[left]
