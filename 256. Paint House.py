# Time:  O(n)
# Space: O(n)
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different. You have to paint all the houses
#  such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example,
# costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1
# with color green, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if costs==None or len(costs)==0:
            return 0

        dp = [[0]*3 for dummy in range(n)]
        dp[0] = costs[0][:]

        for ind in range(1,n):
            dp[ind][0] = costs[ind][0] + min(dp[ind-1][1],dp[ind-1][2])
            dp[ind][1] = costs[ind][1] + min(dp[ind-1][0],dp[ind-1][2])
            dp[ind][2] = costs[ind][2] + min(dp[ind-1][0],dp[ind-1][1])

        return min(dp[-1])