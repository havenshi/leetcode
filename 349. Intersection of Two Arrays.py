class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        ans = []
        for x in nums2:
            if x in set1:
                ans.append(x)
                set1.remove(x)
        return ans