# -*- coding: utf-8 -*-
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
#
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
#
# Example 1:
#
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Example 2:
#
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.
# Follow Up:
# Can you do it in O(n) time?
# import collections
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         ans = sums = 0
#         cnt = collections.Counter()
#         for num in nums:
#             cnt[sums] += 1
#             sums += num
#             ans += cnt[sums - k] # [1, -1, 5, -2]的sum为（[1, -1]的sum）+ k
#             print cnt,sums,ans, sums - k
#         return ans
#
# if __name__ == '__main__':
#     print Solution().subarraySum([1, -1, 5, -2, 3], 3)



# 更加清晰的类似于2sum的解法
class Solution(object):
    def longest_k_sum(self, lst, k):
        kv = {0: -1}
        sum_val = 0
        ans = 0
        for i in range(len(lst)):
            sum_val += lst[i]
            if not kv.get(sum_val):
                kv[sum_val] = i
            if kv.get(sum_val - k) is not None:
                ans = max(ans, i - kv[sum_val - k])
        return ans

if __name__ == "__main__":
    s = Solution()
    print s.longest_k_sum([1, -1, 5, -2, 3, 1, -1], 6)