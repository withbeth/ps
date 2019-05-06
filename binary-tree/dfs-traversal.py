# Traversing a tree means visiting each node in a SPECIFIED order
# This process is NOT as commonly used as finding, inserting and deleting nodes.
# One reason for this is that traversal is not particularly fast.
# Two types of traversal(BFS, DFS)
# Three variants for DFS(pre-order, in-order, post-order)
# In-order traversal : for retrieving all data in sorted order for BST.
# Post-order traversal : for deleting node; you delete its left and right sub-nodes before you delete the node itself.

# Refer
# - 94-medium-in-order-traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/
# - 145-hard-post-order-traversal: https://leetcode.com/problems/binary-tree-postorder-traversal/

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def preorder_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None or root.val == 'null':
            return []
        return [root.val] \
            + self.preorder_recur(root.left) \
            + self.preorder_recur(root.right)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

    def inorder_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorder_recur(root.left) \
            + [root.val] \
            + self.inorder_recur(root.right)

    def inorderTraversal(self, root):
        if len(root) == 0:
            return []
        res = []
        stack = []
        while True:
            # Go to left leaf first
            while root:
                stack.append(root)
                root = root.left
            # Check base condition before pop
            if len(stack) <= 0:
                break
            # Visit
            current = stack.pop()
            if current:
                res.append(current.val)
                root = root.right
        return res


    def postorder_recur(self, root):
        """
        left -> right -> root
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.postorder_recur(root.left) \
            + self.postorder_recur(root.right) \
            + [root.val]

    def postorderTraversal(self, root):
        """
        Using two stacks;
        left -> right -> root
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack1 = [root]
        stack2 = []
        while len(stack1) > 0:
            node = stack1.pop()
            if node:
                stack2.append(node.val)
                stack1.append(node.left)
                stack1.append(node.right)
        res = []
        while len(stack2) > 0:
            res.append(stack2.pop())
        return res



