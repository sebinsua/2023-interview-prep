from typing import List


def rows(grid):
    return iter(grid)


def columns(grid: List[List[str]]):
    return zip(*grid)


def squares(size: int, grid: List[List[str]]) -> List[List[str]]:
    for i in range(0, len(grid), size):
        for j in range(0, len(grid[i]), size):
            yield [grid[x][j : j + size] for x in range(i, i + size)]


def is_sudoku_sequence_valid(sequence: List[str]):
    sequence_without_dots = [num for num in sequence if num != "."]
    return len(set(sequence_without_dots)) == len(sequence_without_dots)


def unnest(nested_list: List[List[str]]) -> List[str]:
    return [item for sublist in nested_list for item in sublist]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for sequence in rows(board):
            if not is_sudoku_sequence_valid(sequence):
                return False

        for sequence in columns(board):
            if not is_sudoku_sequence_valid(sequence):
                return False

        for sequence in map(unnest, squares(3, board)):
            if not is_sudoku_sequence_valid(sequence):
                return False

        return True
