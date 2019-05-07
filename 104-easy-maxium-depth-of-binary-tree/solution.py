# Top-Down Solution
# - Visit the node first to come up with some values.
# - and pass these values to its children when calling the function recursively.
# Bottom-Up Solution
# - Firstly call the functions recursively for all the children.
# - and come up with the answer according to the return values and the value of the root itself.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.top_down_max_depth(root, 1)

    def bottom_up_max_depth(self, node):
        if node is None:
            return 0
        return max(self.bottom_up_max_depth(node.left),
                   self.bottom_up_max_depth(node.right)) \
            + 1

    def top_down_max_depth(self, node, depth):
        if node is None:
            return depth - 1
        ld = self.top_down_max_depth(node.left, depth + 1)
        rd = self.top_down_max_depth(node.right, depth + 1)
        return max(ld, rd)

