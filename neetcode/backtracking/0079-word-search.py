from collections import Counter
from itertools import repeat
from typing import Tuple, List


def get_next_points(board: List[List[str]], point: Tuple[int, int]):
    height = len(board)
    width = len(board[0])

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    new_points = [
        (y + dy, x + dx)
        for (y, x), (dy, dx) in zip(repeat(point), directions)
        if (0 <= y + dy < height and 0 <= x + dx < width)
    ]
    return new_points


class Visited:
    def __init__(self):
        self.visited_set = set()
        self.visited_list = []

    def add(self, triple: Tuple[Tuple[int, int], int, int]):
        point, word_index, depth = triple
        self.visited_set.add(point)
        self.visited_list.append((point, word_index, depth))

    def __contains__(self, point: Tuple[int, int]):
        return point in self.visited_set

    def backtrack(self, depth: int):
        while self.last_depth() >= depth:
            point = self.visited_list.pop()[0]
            self.visited_set.remove(point)

    def last_depth(self):
        return self.visited_list[-1][2] if self.visited_list else float("-inf")


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        # Temporary code to print the board.
        # for y in range(height):
        #     print(''.join(board[y]))

        word_count = Counter(word)
        board_count = Counter(cell for row in board for cell in row)

        # If the board does not have enough of the characters in the
        # word it would be impossible to find the word in the board.
        if any(board_count[char] < word_count[char] for char in word_count.keys()):
            return False

        # If you start with the character that is less common,
        # there are fewer paths that you need to check within
        # the board.
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        for y in range(height):
            for x in range(width):
                visited = Visited()

                start_point = (y, x)
                stack = [(start_point, 0, 0)]
                while stack:
                    point, word_index, depth = stack.pop()

                    # Every iteration that `append`s items to the stack
                    # will provide a newly incremented 0-indexed `depth`
                    # imitating a recursive function stack. This simulates
                    # backtracking, allowing us to unvisit points visited
                    # in the DFS at a greater depth than we are currently
                    # looking at.
                    #
                    # If we didn't do this, `visited` would contain points
                    # from the longer path that we just failed to find the
                    # target word at (the dead-end that implicitly happens
                    # when neither the target word is found or further
                    # candidate points are added to the stack).
                    visited.backtrack(depth)

                    # Check for visited points by comparing the `point` part of each tuple
                    if point in visited:
                        continue

                    visited.add((point, word_index, depth))

                    if board[point[0]][point[1]] != word[word_index]:
                        continue

                    if word_index == len(word) - 1:
                        return True

                    for next_point in get_next_points(board, point):
                        stack.append((next_point, word_index + 1, depth + 1))

        return False
