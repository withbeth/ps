from Queue import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int] *h->l->r
        :type inorder: List[int]  *l->h->r
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        # Use a map for reducing running time of
        # getting a index of certain value of the given in-order list(O(n))
        m = {val: i for i, val in zip(xrange(len(inorder)), inorder)}
        # Use queue instead of slicing the list(python re-creates the list when
        # you do that. or you can use a index of preorder list to get a next elem.
        q = Queue()
        for x in preorder:
            q.put(x)

        def dac(li, ri):
            if li > ri:
                return None
            if q.empty():
                return None
            h = TreeNode(q.get())
            h.left = dac(li, m[h.val] - 1)
            h.right = dac(m[h.val] + 1, ri)
            return h
        return dac(0, len(inorder) - 1)
