class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        w1 = [c for c in s.strip()]
        w2 = [c for c in t.strip()]

        if len(w1) != len(w2):
            return False
        return sorted(w1) == sorted(w2)


