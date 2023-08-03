from typing import Generator, List, Tuple


def is_land(char: str) -> bool:
    return char == "1"


def directions(
    grid: List[List[str]], y: int, x: int
) -> Generator[Tuple[int, int], None, None]:
    height = len(grid)
    width = len(grid[0])

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dy, dx in dirs:
        if (
            (0 <= y + dy < height)
            and (0 <= x + dx < width)
            and is_land(grid[y + dy][x + dx])
        ):
            yield (y + dy, x + dx)


def eat_island(grid: List[List[str]], start: Tuple[int, int]) -> None:
    height = len(grid)
    width = len(grid[0])

    stack = [start]
    while stack:
        y, x = stack.pop()

        grid[y][x] = "0"

        for point in directions(grid, y, x):
            stack.append(point)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])

        islands = 0
        for y in range(height):
            for x in range(width):
                if is_land(grid[y][x]):
                    eat_island(grid, (y, x))
                    islands += 1

        return islands
