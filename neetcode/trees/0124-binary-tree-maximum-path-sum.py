from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root: Optional[TreeNode]) -> List[TreeNode]:
    # In this iterative approach to "post-order" DFS traversal
    # we use a `deque` in order that we do not need to reverse
    # the stack at the end.
    post_order_stack = deque([])

    stack = [root]
    while stack:
        node = stack.pop()

        post_order_stack.appendleft(node)

        # In order to ensure that the "left" subtree is processed
        # prior to the "right" subtree we append the right subtree
        # before the left subtree. As we are appending to a stack
        # the left subtree will be popped before the right subtree.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return iter(post_order_stack)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        # This solution to getting the "maximum path sum" within a binary tree is
        # a bottom-up solution that attempts to compute and then store the maximum
        # path sums at leaf nodes before incrementally moving upwards towards their
        # root nodes.
        node_max_path_sum = {}

        # A "path sum" could be a path from a leaf node up through the `.left` pointer
        # of a node, or it could be a path from a leaf node up through the `.right`
        # pointer of a node, or it could be a V-shaped path that travels up through
        # the `.left` pointer into a node and then down through the `.right` pointer
        # of that node. These paths would exist recursively at every node in the tree
        # and so a resulting path could be more intricate than a mere diagonal line
        # or V-shape as it could made from following this logic at different points in
        # the tree. However, luckily we cannot travel backwards through a node so the
        # path is constrained in that way.
        #
        # We do a "post-order" DFS traversal that ensures that we'll process the
        # children of nodes before we process the nodes themselves. Another method
        # would have been to do a "reverse level-order" traversal but this is less
        # traditional for this kind of problem.
        #
        # In "post-order" traversals we process the left-subtree first, then the
        # right-subtree, before processing the root node. This ensures that the
        # children of the root node have been processed before it.
        for node in postorder(root):
            # We default to `0` values for the max path sums to correctly handle
            # the leaf nodes of the tree.
            max_left_path_sum = node_max_path_sum.get(node.left, 0)
            max_right_path_sum = node_max_path_sum.get(node.right, 0)

            # The maximum path sum could be:
            # - The current value of a root node.
            # - The "best" maximum sum path down the left child and including the
            #   current root node's value.
            # - The "best" maximum sum path down the right child and including the
            #   current root node's value.
            # - The path that includes the current root node's value and the "best"
            #   maximum sum path down the left child and right child.
            max_path_sum_at_node = max(
                node.val,
                node.val + max_left_path_sum,
                node.val + max_right_path_sum,
                node.val + max_left_path_sum + max_right_path_sum,
            )

            # Once we know the maximum possible path sum achievable at a particular
            # node we can use this to attempt to maximize the overall `max_path_sum`.
            max_path_sum = max(max_path_sum, max_path_sum_at_node)

            # We memoize the the maximum path sum against a node so that it can be
            # picked up in future iterations of the post-order traversal in the children
            # of a node (e.g. `node.left` or `node.right`). Originally we start at the
            # leaf nodes of the binary tree. These have no children and therefore use `0`
            # values for each of their maximum left/right path sums.
            #
            # Note: there are ways of writing this with fewer redundant computations
            # but we are prioritizing the expressiveness of the code to make the code
            # easier to understand and improving its educational value.
            node_max_path_sum[node] = max(
                node.val,
                node.val + max_left_path_sum,
                node.val + max_right_path_sum,
            )

        return max_path_sum
