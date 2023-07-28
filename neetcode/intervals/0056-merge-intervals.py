from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals so they are in ascending order by their start value.
        # e.g. [[1, 2], [1, 5], [2, 4], [4, 9], [12, 56]]
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        # This is what we're going to create.
        extended_intervals = []

        # We want to always work with the working interval so we pre-fill this.
        working = sorted_intervals[0]
        # Loop through each of the sorted intervals, grabbing the start and end values.
        for start, end in sorted_intervals:
            # Get the start and end values of the working interval.
            working_start, working_end = working
            # We have an overlapping interval if the current start of an interval is less than
            # or equal to the end of the working/previous interval.
            if start <= working_end:
                # It's possible that although overlapping, the working interval has an end which
                # is greater than the current end.
                if working_end > end:
                    # If this is the case we will leave this working range untouched.
                    pass
                else:
                    # But if the current end is greater than the working end then we should
                    # recreate the working interval but with this extended end.
                    working = [working_start, end]
            else:
                # If the current interval is not overlapping the working interval then this
                # implies that the working interval is now complete and therefore can be pushed
                # into `extended_intervals`.
                extended_intervals.append(working)
                # Finally, we take the new interval and set it against the working interval.
                # This destroys the working interval which should be considered used up
                # since it was placed into `extended_intervals`, and ensures that the current
                # interval is considered by the next loop iteration.
                working = [start, end]

        # Since we only add the previous range into `extended_intervals` on encountering a new
        # interval we always need to add the previous interval into `extended_intervals` on
        # exiting the loop.
        extended_intervals.append(working)

        return extended_intervals
