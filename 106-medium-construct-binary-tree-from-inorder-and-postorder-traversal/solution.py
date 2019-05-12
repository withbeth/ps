# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        Constraints : Duplicates do not exists.
        :type inorder: List[int]   *l->h->r
        :type postorder: List[int] *l->r->h
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        # Using a map for reducing running time of
        # getting a index of certain value of the given in-order list(O(n))
        m = {val: i for i, val in zip(xrange(len(inorder)), inorder)}

        def recur(li, ri):
            if li > ri:
                return None
            # Don't need to check stack(postorder list) size
            # since len(inorder) == len(postorder)
            h = TreeNode(postorder.pop())
            h.right = recur(m[h.val] + 1, ri)
            h.left = recur(li, m[h.val] - 1)
            return h

        return recur(0, len(inorder) - 1)


