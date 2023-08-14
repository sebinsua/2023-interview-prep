from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])

        # Print out matrix for debugging purposes:
        # for row in range(height):
        #     print(" ".join(str(col) for col in heights[row]))

        # We create two matrices of boolean values to store whether the `(y, x)`
        # is reachable from the pacific or the atlantic.
        #
        # We actually know at this point that, in the case of the pacific, the
        # top and left sides can reach the pacific, and in the case of the atlantic
        # the bottom and right sides can reach the atlantic, but we don't update the
        # boolean values here as will do so later on.
        pacific_ocean_reachability = [[False] * width for _ in range(height)]
        atlantic_ocean_reachability = [[False] * width for _ in range(height)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Although there is optimal substructure and overlapping subproblems, we have
        # to use BFS to solve this as a dynamic programming approach that checked
        # diagonals element by element wouldn't allow us to find paths that do not connect
        # to the ocean directly (i.e. that are moving up or left or moving down or right).
        # For example, it's possible for paths to exist that connect to the ocean but that
        # require you to take a long route around the matrix to get there.
        #
        # We start with the boundaries known to be touching a respective ocean and flood-fill
        # from there as if the ocean is rising.
        #
        # The key point is that we must always follow any path towards a current point that
        # is touching the ocean when the new point (1) is currently not connected to the ocean,
        # and (2) is on higher ground. Needing to consider multiple paths means we need to use BFS.
        pacific_queue = deque(
            [(y, 0) for y in range(height)] + [(0, x) for x in range(1, width)]
        )
        while pacific_queue:
            y, x = pacific_queue.popleft()

            pacific_ocean_reachability[y][x] = True

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < height and 0 <= nx < width):
                    continue

                # Skip any neighbours that we know are reachable
                # from the pacific already.
                if pacific_ocean_reachability[ny][nx]:
                    continue

                # The current cell is known to be connected to water,
                # so if we find any neighbouring cells that are on
                # higher-ground to this, we can find a path from these
                # to the ocean.
                #
                # We add them to the queue so we can look at their
                # neighbours and also to cause them to be marked as
                # connected to the ocean.
                if heights[ny][nx] >= heights[y][x]:
                    pacific_queue.append((ny, nx))

        atlantic_queue = deque(
            [(y, width - 1) for y in range(height)]
            + [(height - 1, x) for x in range(width - 1)]
        )
        while atlantic_queue:
            y, x = atlantic_queue.popleft()

            atlantic_ocean_reachability[y][x] = True

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if not (0 <= ny < height and 0 <= nx < width):
                    continue

                # Skip any neighbours that we know are reachable
                # from the atlantic already.
                if atlantic_ocean_reachability[ny][nx]:
                    continue

                # The current cell is known to be connected to water,
                # so if we find any neighbouring cells that are on
                # higher-ground to this, we can find a path from these
                # to the ocean.
                if heights[ny][nx] >= heights[y][x]:
                    atlantic_queue.append((ny, nx))

        return [
            (y, x)
            for y in range(height)
            for x in range(width)
            if pacific_ocean_reachability[y][x] and atlantic_ocean_reachability[y][x]
        ]
