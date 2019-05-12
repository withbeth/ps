# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        # Need this since you can't mutate closure vars in Python < 3 versions
        self.counter = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def is_unival_subtree(node):
            """
            Check and count if given node(subtree) has uni-values by using
            Bottom-Up recursion and Post-Order DFS traversal method
            """
            if node is None:
                return False
            # Leaf node case
            if node.left is None and node.right is None:
                self.counter += 1
                return True
            # Sub-tree cases(left and right)
            is_left_uni_val = node.left is None \
                or (node.left is not None
                    and is_unival_subtree(node.left)
                    and node.left.val == node.val)
            is_right_uni_val = node.right is None \
                or (node.right is not None
                    and is_unival_subtree(node.right)
                    and node.right.val == node.val)
            self.counter += is_left_uni_val & is_right_uni_val
            return is_left_uni_val & is_right_uni_val

        def is_unival_subtree_using_top_down(node, parent_val):
            # Leaf node case
            if node is None:
                return True
            # Check if CHILDREN are unival subtrees or not
            is_left_uni_val = is_unival_subtree_using_top_down(node.left, node.val)
            is_right_uni_val = is_unival_subtree_using_top_down(node.right, node.val)
            if not is_left_uni_val or not is_right_uni_val:
                return False
            self.counter += 1
            # Check if CURRENT node has a unival value or not by comparing the val of parent node
            return node.val == parent_val

        #is_unival_subtree(root)
        if root is None:
            return 0
        is_unival_subtree_using_top_down(root, -1)
        return self.counter


