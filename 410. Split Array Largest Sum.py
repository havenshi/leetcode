class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        # pre_sum = [0, 7, 9, 14, 24, 32]
        sub_sum = lambda i, j: pre_sum[j + 1] - pre_sum[i]

        dp = [[0 for _ in range(m + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][1] = pre_sum[i + 1]
            k = 0
            for j in range(2, min(m + 1, i + 2)): # j表示可以分多少份
                # k in (0, i-1)，如果分拆之后的max(前半段dp[k][j-1]为0~k-1分为j-1份，后半段sub_sum(k+1, i)为0~k的那1份)反而比较小，则k+1
                while k < i - 1 and max(dp[k][j-1], sub_sum(k+1, i)) > max(dp[k+1][j-1], sub_sum(k+2,i)):
                    k += 1
                dp[i][j] = max(dp[k][j - 1], sub_sum(k+1, i))
        return dp[n - 1][m]

if __name__ == "__main__":
    print Solution().splitArray([7,2,5,10,8], 2)