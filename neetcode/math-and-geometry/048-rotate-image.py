from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])

        # Transpose the matrix
        for y in range(height):
            for x in range(y + 1, width):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

        # Reverse each row
        for i in range(height):
            matrix[i] = matrix[i][::-1]
