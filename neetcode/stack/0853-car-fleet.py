from typing import List


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        stack = []

        cars = sorted(
            (
                (position, speed, (target - position) / speed)
                for position, speed in zip(positions, speeds)
            )
        )

        for position, speed, time_to_target in cars:
            if speed == 0:
                continue

            while stack:
                _, _, previous_time_to_target = stack[-1]
                if previous_time_to_target <= time_to_target:
                    stack.pop()
                else:
                    break

            stack.append((position, speed, time_to_target))

        return len(stack)
