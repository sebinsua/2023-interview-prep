from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        max_height = max(height)

        l = 0
        r = len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            width = r - l
            area = max(area, min_height * width)

            # If the area of a hypothetical container with the maximum height
            # and the current width is less than or equal to the largest area
            # found so far, there's no point in continuing the loop, since
            # it's not possible to find a larger area.
            if max_height * width <= area:
                break

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
