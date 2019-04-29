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
        # Key: element, Val : Count
        counts = {}

        def cache(x):
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

        def consume(y):
            if y in counts:
                counts[y] -= 1
                if counts[y] == 0:
                    del counts[y]
                return y
            return None

        map(cache, xs)
        return filter(lambda e: e is not None, map(consume, ys))
