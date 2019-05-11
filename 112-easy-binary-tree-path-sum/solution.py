# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def pre_order(node, prev_sum):
            if node is None:
                return False
            if node.left is None and node.right is None:
                if prev_sum + node.val == sum:
                    return True
                return False
            return pre_order(node.left, prev_sum + node.val) \
                + pre_order(node.right, prev_sum + node.val)

        return pre_order(root, 0)
