from typing import Tuple, List, Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # We create this lookup to avoid having to do a linear search for the `root_node_pointer_in_inorder`
        # which would cause the overall algorithm to be `O(n^2)` time complexity.
        inorder_index_lookup = {value: index for index, value in enumerate(inorder)}

        # You can build a binary tree from a "preorder" and "inorder" traversal
        # as it's possible to find the pointer to the root node in the first
        # index of the "preorder" traversal and then use this to find the root
        # node in the "inorder" traversal, which then allows you (via the sizes
        # of the left and right subtrees) to find the left and right pointers in
        # the "preorder" sequence.
        root_node = TreeNode(preorder[0])
        preorder_slice = (0, len(preorder))
        inorder_slice = (0, len(inorder))
        stack = [(root_node, preorder_slice, inorder_slice)]
        while stack:
            node, preorder_slice, inorder_slice = stack.pop()

            (
                root_node_pointer_in_inorder,
                right_node_pointer_in_inorder,
            ) = self.get_inorder_pointers(
                preorder, preorder_slice, inorder_index_lookup
            )

            # The "preorder" sequence is a bit more complicated to work with as
            # the left and right pointers are not necessarily adjacent to the
            # root node pointer. However, we can use the size of the left subtree
            # to find the left and right pointers in the "preorder" sequence.
            #
            # We also get out some flags that tell us whether the left or right
            # subtrees are empty. This allows us to avoid creating empty subtrees.
            (
                left_node_pointer_in_preorder,
                right_node_pointer_in_preorder,
                is_left_subtree_empty,
                is_right_subtree_empty,
            ) = self.get_preorder_pointers(
                root_node_pointer_in_inorder, preorder_slice, inorder_slice
            )

            _, p_end = preorder_slice
            i_start, i_end = inorder_slice

            if not is_left_subtree_empty:
                node.left = TreeNode(preorder[left_node_pointer_in_preorder])
                # We then append the left node and next "preorder" and "inorder" slices
                # of the left subtree rooted to this node to the stack for further processing.
                stack.append(
                    (
                        node.left,
                        (left_node_pointer_in_preorder, right_node_pointer_in_preorder),
                        (i_start, root_node_pointer_in_inorder),
                    )
                )

            if not is_right_subtree_empty:
                node.right = TreeNode(preorder[right_node_pointer_in_preorder])
                # We then append the left node and next "preorder" and "inorder" slices
                # of the right subtree rooted to this node to the stack for further processing.
                stack.append(
                    (
                        node.right,
                        (right_node_pointer_in_preorder, p_end),
                        (right_node_pointer_in_inorder, i_end),
                    )
                )

        return root_node

    def get_inorder_pointers(
        self,
        preorder: List[int],
        preorder_slice: Tuple[int, int],
        inorder_index_lookup: Dict[int, int],
    ):
        p_start, _ = preorder_slice

        root_node_pointer_in_preorder = p_start

        root_node_pointer_in_inorder = inorder_index_lookup[
            preorder[root_node_pointer_in_preorder]
        ]
        right_node_pointer_in_inorder = root_node_pointer_in_inorder + 1

        return root_node_pointer_in_inorder, right_node_pointer_in_inorder

    def get_preorder_pointers(
        self,
        root_node_pointer_in_inorder: int,
        preorder_slice: Tuple[int, int],
        inorder_slice: Tuple[int, int],
    ):
        p_start, p_end = preorder_slice
        i_start, _ = inorder_slice

        left_subtree_size = root_node_pointer_in_inorder - i_start

        left_node_pointer_in_preorder = p_start + 1
        right_node_pointer_in_preorder = (
            left_node_pointer_in_preorder + left_subtree_size
        )

        is_left_subtree_empty = left_subtree_size <= 0
        is_right_subtree_empty = right_node_pointer_in_preorder >= p_end

        return (
            left_node_pointer_in_preorder,
            right_node_pointer_in_preorder,
            is_left_subtree_empty,
            is_right_subtree_empty,
        )
