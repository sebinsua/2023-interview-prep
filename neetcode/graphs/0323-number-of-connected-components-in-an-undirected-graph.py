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
    def countComponents(self, n: int, edges: List[Tuple[int, int]]) -> int:
        # As this is an undirected graph we can use "union-find" to count the number
        # of connected components.
        uf = UnionFind()

        # When we union nodes with an edge between them, we are connecting them
        # which essentially means pointing them to the same `root` representative.
        for a, b in edges:
            uf.union(a, b)

        # Even though we haven't necessarily inserted all of the nodes within the
        # sequence `0..n-1` (e.g. `range(n)`) we can still find them when we
        # `.find(x)` as this implicitly inserts missing nodes.
        #
        # For the nodes that are connected, they will return the same `root` value
        # from `.find(x)` and this will be deduplicated by the `set()` call, before
        # counting the number of components.
        return len(set(uf.find(x) for x in range(n)))
