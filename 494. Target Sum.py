class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # dp
        import collections
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sgn in (1, -1):
                for k in dp.keys():
                    ndp[k + n * sgn] += dp[k]
            dp = ndp
        return dp[S]

        # hash, TLE
        # self.dictionary = {}
        # res = 0
        #
        # if len(nums) == 1:
        #     if nums[0] == S:
        #         self.dictionary[S] = self.dictionary.get(S, 0) + 1
        #         res += 1
        #     if -nums[0] == S:
        #         self.dictionary[S] = self.dictionary.get(S, 0) + 1
        #         res += 1
        #     return res
        #
        # res += self.findTargetSumWays(nums[1:], S - nums[0])
        # res += self.findTargetSumWays(nums[1:], S + nums[0])
        #
        # self.dictionary[S] = self.dictionary.get(S, 0) + res  # don't forget!
        #
        # return res

        # dfs, O(2^n), TLE
        # if len(nums) == 1:
        #     return sum([1 for x in [1, -1] if nums[0] * x == S])
        # res = 0
        # res += self.findTargetSumWays(nums[1:], S-nums[0])
        # res += self.findTargetSumWays(nums[1:], S+nums[0])
        # return res


        # dfs, O(2^n), TLE
    #     if len(nums) == 1:
    #         return sum([1 for x in [1, -1] if nums[0] * x == S])
    #     res = 0
    #     for item in self.dfs(nums[1:]):
    #         if nums[0] + item == S:
    #             res += 1
    #         if -nums[0] + item == S:
    #             res += 1
    #     return res
    #
    # def dfs(self, nums):
    #     if len(nums) == 1:
    #         return [nums[0], -nums[0]]
    #     return [nums[0] + x for x in self.dfs(nums[1:])] + [-nums[0] + x for x in self.dfs(nums[1:])]

if __name__ == '__main__':
    print Solution().findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47],38)