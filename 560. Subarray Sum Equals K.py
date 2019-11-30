# O(n)
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary = {0: 1}  # 初始化，记录起点到i位置的sum以及出现的次数
        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            res += dictionary.get((total - k), 0)  # 如果能找到sum-k，目前的位置又为sum，一定存在k
            dictionary[total] = dictionary.get(total, 0) + 1  # 注意之前可能已经有total的情况，所以dict的值需要加总

        return res


# MLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = len(nums)
        if not m: return 0
        dp = [[0] * m for _ in range(m)]
        count = 0
        for i in range(m):
            for l in range(m-i):
                if i == 0:
                    dp[i][i+l] = dp[i][i+l-1] + nums[i+l]
                else:
                    dp[i][i+l] = dp[0][i+l] - dp[0][i-1]
                if dp[i][i+l] == k:
                    count += 1
        return count