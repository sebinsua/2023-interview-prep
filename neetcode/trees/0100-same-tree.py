from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Return `True` if both elements are `None`.
        if p is None and q is None:
            return True

        stack = [(p, q)]
        while stack:
            el1, el2 = stack.pop()

            # If any one of the elements is `None` then
            # they cannot be equal so we must return `False`.
            if el1 is None or el2 is None:
                return False

            # If their values are unequal we return `False`.
            if el1.val != el2.val:
                return False

            if el1.left or el2.left:
                stack.append((el1.left, el2.left))
            if el1.right or el2.right:
                stack.append((el1.right, el2.right))

        return True
