# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, root: Node) -> Node:
        if not root:
            return None

        # Basically, we store a pointer from each node to its cloned node,
        # and we then run a DFS traversal of this node and its neighbors
        # through use of a stack.
        cache = {root: Node(root.val)}
        stack = [root]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                # We check our cache for each of the neighbours, and if they are not
                # found we clone them and add them to the cache, so that there is a
                # pointer from the old neighbor to the cloned neighbor.
                if neighbor not in cache:
                    cache[neighbor] = Node(neighbor.val)
                    # We also append each of these neighbours into the stack. The stack
                    # deals with the non-cloned original versions of nodes that are useful
                    # for lookups and contain all of the neighbors.
                    stack.append(neighbor)

                # Finally, we update our cached node with the new cached neighbors
                # that may have been created above.
                cache[node].neighbors.append(cache[neighbor])

        # Finally, we return the cache version of the root node.
        return cache[root]
