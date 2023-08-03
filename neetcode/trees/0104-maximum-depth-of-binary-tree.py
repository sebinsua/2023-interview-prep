from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        stack = [(1, root)]
        while stack:
            depth, el = stack.pop()
            max_depth = max(max_depth, depth)

            if el.left:
                stack.append((depth + 1, el.left))
            if el.right:
                stack.append((depth + 1, el.right))

        return max_depth
