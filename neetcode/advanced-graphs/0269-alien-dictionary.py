from collections import defaultdict, deque
from typing import Any, List, Generator


def create_adjacency_list(words: List[str]) -> defaultdict[str, List]:
    # Ensure that the sequence of words is valid by ensuring
    # that a word is not followed by a shorter word with the
    # same prefix (e.g. "abc" followed by "ab", would imply
    # a sequence that was definitely not lexicographically
    # ordered).
    for previous_word, word in zip(words, words[1:]):
        if len(word) < len(previous_word) and previous_word.startswith(word):
            return None

    # Iterate over the words producing a sequence of tuples
    # containing the prefix and the character at the current
    # index of each word.
    #
    # For example, given the words "abc", "abd", "ade", the
    # sequence of tuples would be:
    #
    # ("", ["a", "a", "a"])
    # ("a", ["b", "b", "d"])
    # ("ab", ["c", "d", "e"])
    def chars_grouped_by_prefix(words):
        max_len = max(map(len, words)) if words else 0
        for i in range(max_len):
            prefix_words = defaultdict(list)
            for word in words:
                if i >= len(word):
                    continue
                prefix = word[:i]
                char = word[i]
                prefix_words[prefix].append(char)
            yield from prefix_words.items()

    # Create an adjacency list from the columns of characters
    # in the words grouped by the prefix of each column.
    #
    # The grouping by prefix ensures that we only infer an
    # ordering in between characters with the same prefix.
    # For example, "abc", "bde" allows you to infer
    # that "a" < "b" but not that "b" < "d".
    adjacency_list: defaultdict[str, List] = defaultdict(list)
    for _, chars in chars_grouped_by_prefix(words):
        for i in range(len(chars)):
            j = i + 1

            # Always add the character to the adjacency list
            # even if it has no edges. This ensures that the
            # topological sort will include all characters.
            if chars[i] not in adjacency_list:
                adjacency_list[chars[i]] = []

            # If there is a next character and it is different
            # from the current character, add an edge from the
            # current character to the next character.
            if j < len(chars) and chars[i] != chars[j]:
                if chars[j] not in adjacency_list[chars[i]]:
                    adjacency_list[chars[i]].append(chars[j])

    return adjacency_list


def topological_sort(
    adjacency_list: defaultdict[Any, List]
) -> Generator[str, None, None]:
    # In order to perform a topological sort, we need to
    # keep track of the in-degree of each vertex.
    #
    # The in-degree of a vertex is the number of edges that
    # point to it, and is used to determine which vertexes
    # can be visited next.
    in_degree = {char: 0 for char in adjacency_list}
    for vertex in adjacency_list:
        for edge in adjacency_list[vertex]:
            in_degree[edge] += 1

    topological_order_count = 0

    # We keep a separate queue for the start vertexes because
    # we only want to pick a new start vertex when we've
    # fully traversed the current start vertex.
    #
    # This is helpful for the case in which there are
    # multiple disconnected graphs in the adjacency list
    # but also for the case in which we need to add the
    # characters that we have no ordering information for
    # lexicographically.
    start_vertexes = deque([vertex for vertex in in_degree if in_degree[vertex] == 0])
    queue = deque()
    while queue or start_vertexes:
        if not queue:
            queue.append(start_vertexes.popleft())
        vertex = queue.popleft()

        # A topological sort is performed by traversing through
        # the graph yielding vertexes with an in-degree of 0,
        # and then decrementing the in-degree of each of its
        # edges until they also have an in-degree of 0 and can
        # be added to the queue themselves.
        yield vertex
        topological_order_count += 1

        for edge in adjacency_list[vertex]:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                queue.append(edge)

    # If the number of vertexes in the topological order
    # is not equal to the number of vertexes in the graph,
    # then there is a cycle in the graph.
    if topological_order_count != len(adjacency_list):
        raise ValueError("Cycle detected")


def alien_dictionary(words: List[str]) -> str:
    adjacency_list = create_adjacency_list(words)
    if not adjacency_list:
        return ""

    try:
        return "".join(topological_sort(adjacency_list))
    except ValueError:
        return ""


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        return alien_dictionary(words)


# Empty list
print(alien_dictionary([]))

# Single word
print(alien_dictionary(["abc"]))

# Single letters only
print(alien_dictionary(["z", "x"]))

# Disconnected single letters
print(alien_dictionary(["abc", "b", "d"]))

# Same starting letter
print(alien_dictionary(["az", "ac", "bx", "by"]))

# Same prefixes
print(alien_dictionary(["abc", "abd", "ade"]))

# Disconnected graph
print(alien_dictionary(["abc", "def"]))

# Handling lexicographic order and ambiguity
print(alien_dictionary(["abc", "ace", "bdf"]))

# Letters with the same rank
print(alien_dictionary(["wrt", "wrf", "er", "ett", "rftt"]))

# Invalid dictionary (cycle detection)
print(alien_dictionary(["abc", "bcd", "adb"]))

# Invalid dictionary (shorter word after longer word with prefix)
print(alien_dictionary(["abc", "ab"]))

# Different prefixes but shared postfixes
print(alien_dictionary(["xyz", "ayz", "byz"]))

# More complex cycles
print(alien_dictionary(["a", "ba", "cba", "dcba", "edcba", "de"]))
