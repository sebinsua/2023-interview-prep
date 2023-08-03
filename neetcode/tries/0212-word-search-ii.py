from typing import List
from itertools import repeat


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
        # In order to ensure optimal performance we remove words from the trie
        # as we find them in the board. We can make this optimization to this problem
        # because we only need to find unique words in the board.
        node = self.root

        # List to keep track of nodes to check for deletion.
        nodes_to_check = []
        for char in word:
            # We cannot remove a word if it is not found in the trie.
            if char not in node.children:
                return

            # Decrement the reference count.
            node.children[char].count -= 1

            # We keep track of the parent node and the character in order to
            # delete the child node if it is no longer needed.
            parent = node
            nodes_to_check.append((parent, char))

            node = node.children[char]

        # Check the nodes in reverse order and delete any with a count of 0.
        for parent, char in reversed(nodes_to_check):
            child_node = parent.children[char]
            if child_node.count == 0:
                del parent.children[char]

    def has_prefix(self, char: str, node: TrieNode = None):
        # Unlike other implementations of tries, we provide a much more granular
        # method for checking if a prefix is in the trie, which takes only a single
        # character and a node as arguments. This allows you to re-use nodes that
        # you've already found in the trie, and avoids the need to traverse the trie
        # from the root every time you want to check if a prefix is in the trie.
        node = node if node is not None else self.root

        if char not in node.children:
            return None

        return node.children[char]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        height = len(board)
        width = len(board[0])

        # Temporary code to print the board:
        # for i in range(height):
        #     print(''.join(board[i]))

        # First, we add all the words to a trie.
        # We need the trie to speed up checking if a word is in the board.
        trie = Trie()
        for word in words:
            trie.add_word(word)

        # We only need to return unique words so we use a set to store the words found.
        words_found = set([])

        # We iterate through the board, checking whether the first character is in the trie.
        for y in range(height):
            for x in range(width):
                first_char = board[y][x]

                start_node = trie.has_prefix(first_char)
                if not start_node:
                    continue

                # If the first character is in the trie, we check whether this is a standalone
                # word in the trie, as if it is we can add it into the set.
                if start_node.is_end_of_word:
                    words_found.add(first_char)

                # We then do a DFS to check if the word is in the board, starting from the
                # initial point and keeping track of the node (in order to speed up the `.has_prefix`
                # method) and the current word (in order to add it into the `words_found` set if it
                # is a word in the trie).
                #
                # We also keep track of the visited points for a particular path, so that we don't
                # accidentally travel back to a point we've already visited.
                initial_point = (y, x)
                initial_visited = set([initial_point])
                stack = [(initial_point, start_node, first_char, initial_visited)]
                while stack:
                    point, node, current_prefix, visited = stack.pop()

                    # We check the four directions from the current point,
                    # while ensuring that we do not go out of bounds.
                    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                    new_points = [
                        (y + dy, x + dx)
                        for (y, x), (dy, dx) in zip(repeat(point), directions)
                        if (0 <= y + dy < height and 0 <= x + dx < width)
                    ]
                    for new_point in new_points:
                        # If the new point is already visited, skip it.
                        if new_point in visited:
                            continue

                        new_y, new_x = new_point
                        next_char = board[new_y][new_x]
                        next_node = trie.has_prefix(next_char, node)
                        # If the new point is not in the trie, skip it.
                        if not next_node:
                            continue

                        next_prefix = f"{current_prefix}{next_char}"
                        # If the new point is in the trie, check to see if it is a word,
                        # and add it to the set if it is.
                        if next_node.is_end_of_word:
                            words_found.add(next_prefix)
                            # We also remove the word from the trie to optimize later searches
                            # while also incidentally ensuring that all words added to the set
                            # are unique.
                            trie.remove_word(next_prefix)

                        # We copy the visited set and add the new point to this in order that
                        # we don't accidentally visit the same point twice and to ensure that
                        # we avoid mutating the visited set of the other paths in our stack.
                        visited_copy = visited.copy()
                        visited_copy.add(new_point)

                        # We add the new point, next node, next prefix, and visited set to the stack,
                        # so that we can continue the DFS.
                        stack.append(
                            (
                                new_point,
                                next_node,
                                next_prefix,
                                visited_copy,
                            )
                        )

        return words_found
