class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product = 1
        ll = rr = -1
        ans = 0
        for num in nums:
            rr += 1
            product *= num
            while ll + 1 <= rr and product >= k:
                product /= nums[ll + 1]
                ll += 1
            ans += rr - ll
        return ans