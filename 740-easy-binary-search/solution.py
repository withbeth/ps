class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int] - sorted(in ascending order)
        :type target: int
        :rtype: int - index of the given target if target exists. otherwise return -1
        """
        if len(nums) == 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            assert l <= m
            assert m <= r
            if nums[m] == target:
                return m
            elif nums[m] < target:
                # Only update left
                l = m + 1
            else:
                # Only update right
                r = m - 1
        return -1


    def contains(self, nums, target):
        """
        :type nums: List[int] - sorted(in ascending order)
        :type target: int
        :rtype: bool - true if target exists. otherwise return False
        """
        if len(nums) <= 0:
            return False
        m = len(nums) // 2
        if nums[m] == target:
            return True
        elif nums[m] < target:
            assert m+1 <= len(nums)-1, "Middle index should be equal or less than Right index"
            return self.contains(nums[m + 1:], target)
        assert 0 <= m, "Middle index should be equal or less than Middle index"
        return self.contains(nums[:m], target)


