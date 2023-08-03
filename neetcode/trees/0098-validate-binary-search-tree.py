from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        elements = []

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
            elements.append(current.val)

            # Move to the right child to continue traversal.
            current = current.right

        for i in range(1, len(elements)):
            if elements[i] <= elements[i - 1]:
                return False

        return True
