#! /bin/python
class Solution(object):

    # Constraint
    # list1, list2 can have duplicated elements
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 == nums2:
            return nums1
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        return self.f(nums1, nums2)

    def f(self, xs, ys):
        res = []
        # Key: element, Val : Count
        counts = {}
        # Cache
        for x in xs:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        # Consume
        for y in ys:
            if y in counts:
                res.append(y)
                counts[y] -= 1
                if counts[y] == 0:
                    del counts[y]
        return res

