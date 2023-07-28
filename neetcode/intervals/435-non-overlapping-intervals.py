from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])

        count = 0
        previous_end = intervals[0][1]
        for i in range(1, n):
            if previous_end > intervals[i][0]:
                count += 1
            else:
                previous_end = intervals[i][1]

        return count
