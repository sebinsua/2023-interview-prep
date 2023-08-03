from typing import Optional, Generator


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def in_order(self, root: Optional[TreeNode]) -> Generator[int, None, None]:
        # Start traversal from the root of the binary tree.
        current = root
        stack = []
        while current or stack:
            # Go to the leftmost node, adding nodes to the stack.
            while current:
                stack.append(current)
                current = current.left

            # Visit the current node (leftmost node in the stack).
            current = stack.pop()

            yield current.val

            # Move to the right child to continue traversal.
            current = current.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_values = self.in_order(root)

        kth_smallest: int
        for _ in range(k):
            kth_smallest = next(smallest_values)

        return kth_smallest
