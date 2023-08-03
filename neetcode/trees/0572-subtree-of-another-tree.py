class Solution:
    def isSubtree(self, main_tree: TreeNode, subtree: TreeNode) -> bool:
        # This function performs a Depth-First Search (DFS) on the
        # main_tree. It starts by pushing the root of the main_tree
        # onto the main_stack.
        main_stack = [main_tree]

        while main_stack:
            current_node = main_stack.pop()

            # For each node in the main_tree, if its value matches the
            # root value of the subtree, the algorithm will initiate
            # a second DFS to check if this node's entire subtree
            # matches the given subtree.
            if current_node.val == subtree.val:
                subtree_stack = [(current_node, subtree)]
                while subtree_stack:
                    main_node, sub_node = subtree_stack.pop()

                    # If the values of the main_node and sub_node are
                    # not the same, this will break the inner while loop.
                    if main_node and sub_node:
                        if main_node.val != sub_node.val:
                            break

                        # If the nodes match, it continues by pushing their
                        # children to the subtree_stack for further matching.
                        subtree_stack.append((main_node.right, sub_node.right))
                        subtree_stack.append((main_node.left, sub_node.left))
                    elif main_node or sub_node:
                        break
                else:
                    # The else clause corresponds to the while loop. It will
                    # execute when the while loop completes normally (no breaks).
                    # This means that all nodes of the subtree match the
                    # corresponding nodes in the main_tree.
                    return True

            # If the current node's value doesn't match the subtree's root,
            # or if the subtree matching was unsuccessful, it continues the
            # DFS on the main_tree.
            if current_node.left:
                main_stack.append(current_node.left)
            if current_node.right:
                main_stack.append(current_node.right)

        # If it has checked all nodes in the main_tree and hasn't returned
        # True, this means that the subtree doesn't exist in the main_tree.
        return False
