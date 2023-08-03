from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

        node.is_end_of_word = True

    def remove_word(self, word: str):
        node = self.root

        # List to keep track of nodes to check for deletion.
        nodes_to_check = []
        for char in word:
            # Word not found in trie
            if char not in node.children:
                return
            parent, node = node, node.children[char]
            nodes_to_check.append((parent, char))
            # Decrement the count.
            node.count -= 1

        # Check nodes in reverse order and delete if count is 0.
        for parent, char in reversed(nodes_to_check):
            child_node = parent.children[char]
            if child_node.count == 0:
                del parent.children[char]

    def has_prefix(self, char: str, node: TrieNode = None):
        node = node if node is not None else self.root

        if char not in node.children:
            return None

        return node.children[char]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        height = len(board)
        width = len(board[0])

        # for i in range(height):
        #     print(''.join(board[i]))

        trie = Trie()
        for word in words:
            trie.add_word(word)

        words_found = set([])

        for y in range(height):
            for x in range(width):
                first_char = board[y][x]

                if not trie.has_prefix(first_char):
                    continue

                initial_point = (y, x)
                initial_visited = set([initial_point])
                start_node = trie.has_prefix(first_char)

                if start_node.is_end_of_word:
                    words_found.add(first_char)

                stack = [(initial_point, start_node, first_char, initial_visited)]
                while stack:
                    point, node, current_word, visited = stack.pop()

                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    for dy, dx in directions:
                        new_y = point[0] + dy
                        new_x = point[1] + dx
                        new_point = (new_y, new_x)

                        if new_point in visited:
                            continue
                        if not (0 <= new_y < height and 0 <= new_x < width):
                            continue

                        next_char = board[new_y][new_x]
                        next_node = trie.has_prefix(next_char, node)
                        if not next_node:
                            continue

                        if next_node.is_end_of_word:
                            new_word = f"{current_word}{next_char}"
                            words_found.add(new_word)
                            trie.remove_word(new_word)

                        visited_copy = visited.copy()
                        visited_copy.add(new_point)

                        stack.append(
                            (
                                new_point,
                                next_node,
                                f"{current_word}{next_char}",
                                visited_copy,
                            )
                        )

        return words_found
