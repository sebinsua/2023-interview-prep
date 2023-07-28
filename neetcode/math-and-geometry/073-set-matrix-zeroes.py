from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        height = len(matrix)
        width = len(matrix[0])

        zero_rows = set()
        zero_columns = set()

        # Find zeroes and store their row and column indexes.
        for row in range(height):
            for col in range(width):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_columns.add(col)

        # Set rows to zero.
        for row in zero_rows:
            matrix[row] = [0] * width

        # Set columns to zero.
        for col in zero_columns:
            for row in matrix:
                row[col] = 0

        return matrix