from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        values = []

        # We use a "level-order" BFS traversal.
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                values.append("N")
                continue

            values.append(node.val)

            queue.append(node.left)
            queue.append(node.right)

        return ",".join(str(value) for value in values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = deque(data.split(","))
        root_str_value = values.popleft()
        if root_str_value == "N":
            return None

        root = TreeNode(int(root_str_value))

        # We use a "level-order" traversal to take our "level-order"
        # queue and construct a binary tree from it. Internally
        # we pop twice after getting a parent or root node to get
        # the left and right value, and if these are non-"N" link
        # these nodes to the parent and append them to the queue
        # for further traversal.
        #
        # If you include NULL nodes in the serialization, you can
        # generally use the same traversal method for both serialization
        # and deserialization. Without NULL nodes, the process is
        # typically more complex, and requires additional information
        # such as combining different types of traversals. For instance,
        # you might need both the pre-order and in-order traversals of
        # a binary tree to accurately reconstruct it.
        queue = deque([root])
        while queue:
            parent = queue.popleft()

            left_value = values.popleft()
            if left_value != "N":
                parent.left = TreeNode(int(left_value))
                queue.append(parent.left)

            right_value = values.popleft()
            if right_value != "N":
                parent.right = TreeNode(int(right_value))
                queue.append(parent.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
