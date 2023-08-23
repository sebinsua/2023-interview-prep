from typing import List, Tuple


class UnionFind:
    def __init__(self):
        self.representatives = {}
        self.ranks = {}

    def find(self, x: int):
        # If `x` is not in the representatives, initialize it.
        if x not in self.representatives:
            self.representatives[x] = x
            self.ranks[x] = 0

        # We find the `root` of `x` by traversing upwards until
        # we find a node that points to itself.
        root = x
        while self.representatives[root] != root:
            root = self.representatives[root]

        # Upon finding the `root` of `x`, we update
        # the representatives of all nodes along the path.
        # This is called path compression, and optimizes
        # future calls to `.find(x_n)`.
        while self.representatives[x] != x:
            parent = self.representatives[x]
            self.representatives[x] = root
            x = parent

        return root

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are the same, then `x` and `y` are already connected.
        if root_x == root_y:
            return

        rank_x, rank_y = self.ranks[root_x], self.ranks[root_y]

        # If the ranks are the same, then we arbitrarily choose one to be the
        # representative and increment its rank.
        if rank_x == rank_y:
            self.representatives[root_y] = root_x
            self.ranks[root_x] += 1
            return

        # Otherwise, if the ranks are different, then we choose the one with
        # the higher rank to be the representative.
        if rank_x > rank_y:
            self.representatives[root_y] = root_x
            return
        if rank_x < rank_y:
            self.representatives[root_x] = root_y
            return


class Solution:
    def valid_tree(self, n: int, edges: List[Tuple[int]]) -> bool:
        """
        @param n: An integer
        @param edges: a list of undirected edges
        @return: true if it's a valid tree, or false
        """

        uf = UnionFind()
        for e1, e2 in edges:
            # An edge is redundant if it is already connected in the union-find.
            if uf.find(e1) == uf.find(e2):
                return False

            uf.union(e1, e2)

        # A tree is valid if there is only one connected component.
        return len({uf.find(i) for i in range(n)}) == 1


solution = Solution()

# Test case 1: Valid tree with a single node (trivial case)
assert (solution.valid_tree(1, [])) == True

# Test case 2: Valid tree with 4 nodes and 3 edges
assert (solution.valid_tree(4, [[0, 1], [1, 2], [2, 3]])) == True

# Test case 3: Invalid tree with a cycle
assert (solution.valid_tree(3, [[0, 1], [1, 2], [2, 0]])) == False

# Test case 4: Invalid tree with disconnected components
assert (solution.valid_tree(4, [[0, 1], [2, 3]])) == False
