from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            # Popping from the end of the stack makes this a DFS approach.
            # If we want to change to BFS, swap the stack for a `deque`.
            el = stack.pop()
            el.left, el.right = el.right, el.left

            if el.left:
                stack.append(el.left)
            if el.right:
                stack.append(el.right)

        return root
