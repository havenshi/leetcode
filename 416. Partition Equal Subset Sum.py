class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2: return False
        target = sum(nums) / 2
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            newdp = dp[:]
            for i in range(num, target + 1):
                newdp[i] += dp[i - num]  # 注意不能直接变动dp，要用newdp记录
            dp = newdp

        return dp[-1] >= 2  # 为啥不是==2，因为如果数字重复，但是组合还是可以有很多种，如[1,1,1,1]2的组合是6，远大于2