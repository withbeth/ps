#! /bin/python
class Solution(object):
    # Constraint
    # nums1, nums2 can have duplicated elements.
    # Diff with 350 - Each element in the result must be UNIQUE.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
