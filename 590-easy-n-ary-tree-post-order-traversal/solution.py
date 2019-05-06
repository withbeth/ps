class Solution(object):
    def postorder(self, root):
        """
        :type root: Node which has val, children as properties
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                res.append(current.val)
                map(stack.append, current.children)
        return res[::-1]

