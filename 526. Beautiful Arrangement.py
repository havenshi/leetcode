class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.dictionary = dict()
        return self.dfs(1, range(1, N + 1))  # 递归实现，用1~N去替换每一位

    def dfs(self, idx, nums):
        if not nums:
            return 1
        key = idx, tuple(nums)
        if key in self.dictionary:
            return self.dictionary[key]
        ans = 0
        for i, n in enumerate(nums):
            if n % idx == 0 or idx % n == 0:  # (1,(1,2,3))如果1能被nums中的数字整除，交换
                ans += self.dfs(idx + 1, nums[:i] + nums[i + 1:])  # 1交换之后，下一步是2交换
        self.dictionary[key] = ans
        return ans