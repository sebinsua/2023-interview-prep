from operator import itemgetter
from typing import List, Tuple

class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        intervals.sort(key=itemgetter(0))

        for (_, previous_end), (current_start, _) in zip(intervals, intervals[1:]):
            if previous_end > current_start:
                return False

        return True