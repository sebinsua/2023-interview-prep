from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], new_interval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [new_interval]

        new_left, new_right = new_interval

        results = []
        to_insert = True
        for left, right in intervals:
            # If the new interval is within the current interval
            # it is contained by this and we should mark `to_insert`
            # as `False` so it will not be inserted.
            if left < new_left < right and left < new_right < right:
                to_insert = False
                results.append([left, right])
                continue

            # When the left of the new interval intersects with an interval
            # we should alter its left-side to the left of the interval it
            # intersects with.
            if left <= new_left <= right:
                new_left = left

            # When the right of the new interval intersects with an interval
            # we should alter its right-side to the right of the interval it
            # intersects with.
            if left <= new_right <= right:
                new_right = right

            # If the current interval starts after the new interval and it's
            # not yet been inserted we should insert it.
            if to_insert and new_right < left:
                results.append([new_left, new_right])
                to_insert = False

            # Insert the current interval as long as it is not within the new interval.
            if not (new_left <= left <= new_right and new_left <= right <= new_right):
                results.append([left, right])

        # If we've finished looping but haven't yet inserted the interval, append it.
        if to_insert:
            results.append([new_left, new_right])
            to_insert = False

        return results
