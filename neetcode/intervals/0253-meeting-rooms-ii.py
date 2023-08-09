from itertools import accumulate
from typing import List, Tuple

class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int]]) -> int:
        if not intervals:
            return 0
        
        start_times = ((start, 1) for start, _ in intervals)
        end_times = ((end, -1) for _, end in intervals)
        times = sorted(list(start_times) + list(end_times))

        min_meeting_rooms = max(accumulate(delta for _, delta in times))

        return min_meeting_rooms

if __name__ == "__main__":
    solution = Solution()

    intervals1 = [(0, 30), (5, 10), (15, 20)]
    print(solution.minMeetingRooms(intervals1))  # Expected output: 2

    intervals2 = [(7, 10), (2, 4)]
    print(solution.minMeetingRooms(intervals2))  # Expected output: 1

    intervals3 = [(1, 5), (2, 6), (3, 7)]
    print(solution.minMeetingRooms(intervals3))  # Expected output: 3

    intervals4 = [(1, 5), (5, 10), (10, 15), (15, 20)]
    print(solution.minMeetingRooms(intervals4))  # Expected output: 1
