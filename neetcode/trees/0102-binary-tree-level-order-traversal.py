from typing import List, Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)

        queue = deque([(0, root)])
        while queue:
            level, el = queue.popleft()

            levels[level].append(el.val)

            if el.left:
                queue.append((level + 1, el.left))
            if el.right:
                queue.append((level + 1, el.right))

        return levels.values()
