# -*- coding: utf-8 -*-
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different. You have to paint
# all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix.
# For example, costs0 is the cost of painting house 0 with color 0; costs1 is the cost of
# painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Follow up:
# Could you solve it in O(nk) runtime?

# 只需要记录下每个house的最小的两个颜色。
# 如果下一个颜色跟这个颜色不一样，就取最小的这个颜色加上这次所选的颜色，并找出最小值；
# 如果下一个颜色跟这个颜色一样，那么我们不可以取最小的这个颜色，所以我们取第二小的颜色加上这次所选的颜色。
# 最后把最小的颜色输出就可以了

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if costs==None or len(costs)==0:
            return 0
        k = len(costs[0])

        dp = [[0]*k for x in range(n)]
        dp[0] = costs[0][:]
        for i in range(1,n):
            array = sorted(dp[i-1])
            last1 = dp[i-1].index(array[0])
            last2 = dp[i-1].index(array[1])
            for j in range(k):
                if last1 != j:
                    dp[i][j] = dp[i-1][last1] + costs[i][j]
                else:
                    dp[i][j] = dp[i-1][last2] + costs[i][j]
            print dp
        return min(dp[-1])

if __name__ == '__main__':
    answer = Solution()
    print answer.minCostII([[1,2,3],[2,1,5],[4,1,5]])