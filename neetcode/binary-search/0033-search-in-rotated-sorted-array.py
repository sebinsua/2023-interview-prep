from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Special case for lists with only one or two elements.
        if len(nums) <= 2:
            try:
                return nums.index(target)
            except:
                return -1

        # As the array has been sorted and then rotated, it's not actually
        # correctly sorted and we can't use a binary search in the conventional
        # way. However, we do know that the side that contains the rotation
        # will be unsorted while the side that doesn't will be sorted. This
        # is enough for us to perform a modified binary search, which checks
        # if the target is within the sorted side normally, but otherwise
        # assumes it must be within the unsorted side.
        #
        # Example: [6, 7, 1, 2, 3, 4, 5]
        # Left-side (6, 7, 1), Mid Point (2), Right-side (3, 4, 5)
        # Rotation point (1) is found within the left-side therefore
        # the right-side is sorted.
        #
        # Example: [3, 4, 5, 6, 7, 1, 2]
        # Left-side (3, 4, 5), Mid Point (6), Right-side (7, 1, 2)
        # Rotation point (1) is found within the right-side therefore
        # the left-side is sorted.
        left = 0
        right = len(nums) - 1
        while left <= right:
            # We bias the midpoint to the right, as otherwise `// 2` can
            # cause us to be biased towards the left-side.
            mid = left + ((right - left + 1) // 2)

            # If we have found the target return the index.
            if nums[mid] == target:
                return mid

            # Identify which side of the array is sorted.
            # 1. If the mid element is greater than right element,
            #    it means that the array was rotated in the right-side,
            #    and therefore the left-side is sorted.
            # 2. If not the rotation (if any) happened in the left-side,
            #    and therefore the right-side is sorted.
            sorted_side = "left" if nums[mid] > nums[right] else "right"

            match sorted_side:
                case "left":
                    # Check to see whether the target is within the sorted left-side.
                    # If it is, we move to the left-side by adjusting `right` so it is
                    # to the left of the mid (which we already know isn't the target),
                    # otherwise we adjust the `left` to the right of the mid.
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                case "right":
                    # Check to see whether the target is within the sorted right-side.
                    # If it is, we move to the right-side by adjusting `left` so it is
                    # to the right of the mid (which we already know isn't the target),
                    # otherwise we adjust the `right` to the left of the mid.
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

        # If we haven't found the target in the array return -1.
        return -1
