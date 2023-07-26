from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            # As we iterate from both left-to-right and
            # right-to-left we need to keep track of the
            # maximum heights we have seen.
            #
            # The reason for this is that when we calculate
            # the trapped water, the height of that water
            # does not relate to the black sections on either
            # side of it (e.g. n-1 or n+1) but to the heights
            # of the black section seen so far. An analogy
            # that helps explain this is to imagine a pothole
            # in a valley -- if you wanted to fill this up,
            # you would care more about the height of the valley
            # than the height of the pothole.
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # In comparison with similar problems in which we
            # are calculating the area between two sides, in this
            # problem we are computing the amount of water trapped
            # in an elevation map, and therefore we can't just
            # multiply the height by a width, but need to consider
            # how the water has filled each crevice of the elevation
            # map.
            #
            # We do this by calculating the height of the water at
            # each index (e.g. left or right) and removing from this
            # the height of any black section when the water starts
            # above this. The computation is very granular as we only
            # consider the height of one index per iteration of the
            # while loop.
            #
            # When the height of the left index is less than the height
            # of the right index we compute the left height (and increment
            # left), but when the height of the right index is greater
            # than or equal to the left index we compute the right
            # height (and decrement right). Note that this is actually
            # much more counterintuitive than it might appear at first
            # glance, as in practice what it means is that when you find
            # a tall wall using the left pointer, you ignore this height
            # and instead repeatedly move from right-to-left towards it
            # while adding the tallest right height minus the current
            # elevation height. (And the reverse when you find a tall wall
            # using the right pointer.)
            if height[left] < height[right]:
                total += left_max - height[left]
                left += 1
            else:
                total += right_max - height[right]
                right -= 1

        return total
