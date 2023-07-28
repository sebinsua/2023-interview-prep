from typing import List
from itertools import cycle


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        size = len(matrix) * len(matrix[0])

        directions = cycle(["right", "down", "left", "up"])

        min_y, max_y = 0, len(matrix) - 1
        min_x, max_x = 0, len(matrix[0]) - 1
        y, x = 0, 0
        direction = next(directions)
        while min_y <= y <= max_y and min_x <= x <= max_x and len(result) < size:
            result.append(matrix[y][x])

            match direction:
                case "right":
                    if x == max_x:
                        min_y += 1
                        y += 1
                        direction = next(directions)
                    else:
                        x += 1
                case "down":
                    if y == max_y:
                        max_x -= 1
                        x -= 1
                        direction = next(directions)
                    else:
                        y += 1
                case "left":
                    if x == min_x:
                        max_y -= 1
                        y -= 1
                        direction = next(directions)
                    else:
                        x -= 1
                case "up":
                    if y == min_y:
                        min_x += 1
                        x += 1
                        direction = next(directions)
                    else:
                        y -= 1

        return result
