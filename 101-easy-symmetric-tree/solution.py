from Queue import Queue
# refer : https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror_iter(root)

    def is_mirror(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return node1.val == node2.val \
            and self.is_mirror(node1.left, node2.right) \
            and self.is_mirror(node1.right, node2.left)

    def is_mirror_iter(self, root):
        q = Queue()
        q.put((root, root))
        while not q.empty():
            node1, node2 = q.get()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None:
                return False
            # IMPORTANT! Should not use "is not" operator
            # when you compare int values...
            if node1.val != node2.val:
                return False
            q.put((node1.left, node2.right))
            q.put((node1.right, node2.left))
        return True
