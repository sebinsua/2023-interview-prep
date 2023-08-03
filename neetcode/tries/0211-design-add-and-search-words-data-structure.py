class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word) -> None:
        # Insert a word into the trie as usual.
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word) -> bool:
        # Because we need to handle wildcards this is more complicated than normal.
        # We use a `search_space`. By default in the case of a word with no
        # wildcards, it will remain a one-node search space as long as each character is
        # found within the trie. But if there are wildcards involved it can contain
        # multiple nodes. On every iteration we replace this search space with the children
        # matched.
        search_space = [self.root]
        idx = 0
        while search_space and idx < len(word):
            char = word[idx]

            # The `search_space` will be replaced with all of the children matched
            # by the character, and, on every iteration, considers all of the nodes found
            # within it, which were added in a previous iteration.
            #
            # In the simplest case of no wildcards, the search space is either `[]` or
            # `[node.children[char]]`. But if there are wildcards, it's `node.children.values()`.
            #
            # For example, if a previous wildcard caused the search space to contain 5 children,
            # and the next character is "a", the code inside the loop will check each of
            # those 5 node's to see if any of their `.children` properties contain an "a".
            # If they do, the corresponding child nodes for each matching "a" will be added
            # to the new search space for the next iteration.
            def get_next_nodes(node, char):
                if char == ".":
                    return node.children.values()
                if char in node.children:
                    return [node.children[char]]
                return []

            search_space = [
                child for node in search_space for child in get_next_nodes(node, char)
            ]
            idx += 1

        # We have to handle three possibilities:
        # - 0-node search space:   Always returns `False` as this means we could not find either
        #                          the character in our trie or any characters in the case of
        #                          a wildcard.
        # - 1-node search space:   Returns `True` if this node is the end of the word.
        #                          Occurs if the last character of the word matched the trie.
        # - N-node search space:   Returns `True` is any nodes are the end of the word.
        #                          Occurs if the last character of the word was a wildcard.
        return any(node.is_end_of_word for node in search_space)


class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        return self.trie.add_word(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
