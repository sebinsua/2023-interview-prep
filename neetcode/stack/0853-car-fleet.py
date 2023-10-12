from typing import List


class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = [
            (target - position) / speed
            for position, speed in sorted(
                (
                    (position, speed)
                    for position, speed in zip(positions, speeds)
                    if speed != 0
                ),
                key=lambda x: x[0],
            )
        ]

        fleet = []
        for time_to_target in cars:
            while fleet and fleet[-1] <= time_to_target:
                fleet.pop()

            fleet.append(time_to_target)

        return len(fleet)
