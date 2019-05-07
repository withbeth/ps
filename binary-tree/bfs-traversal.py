from Queue import Queue
# refer : https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.iterative_level_order(root)

    def iterative_level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = [[root.val]]
        q = Queue()
        q.put([root.left, root.right])
        while not q.empty():
            curr_res = []
            next_nodes = []
            for node in q.get():
                if node:
                    curr_res.append(node.val)
                    next_nodes.append(node.left)
                    next_nodes.append(node.right)
            if len(next_nodes) > 0:
                q.put(next_nodes)
            if len(curr_res) > 0:
                res.append(curr_res)
        return res
