# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

# dfs + hash
from fractions import Fraction
import collections
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        self.visits = collections.defaultdict(list)
        return 24 in self.dfs(nums)

    def dfs(self, nums):
        if str(sorted(nums)) in self.visits:
            return self.visits[str(nums)]
        n = len(nums)
        if n == 1:
            self.visits[str(sorted(nums))] = [nums[0]]
            return [nums[0]]
        ans = set([])
        for i in range(n):
            for length in range(1, n): # separate nums into part1 and part2 which has different length
                part1 = self.dfs(nums[i:i+length])
                for p1 in part1:       # p1 +-*/ p2
                    part2 = self.dfs(nums[:i]+nums[i+length:])
                    for p2 in part2:
                        tmp = set([p1 + p2, p1 - p2, p2 - p1, p1 * p2])
                        ans |= tmp
                        if p2 != 0:
                            tmp = set([Fraction(p1, p2)])  # fraction of p1/p2
                            ans |= tmp
                        if p1 != 0:
                            tmp = set([Fraction(p2, p1)])  # fraction of p2/p1
                            ans |= tmp
        self.visits[str(sorted(nums))] = list(ans)
        return list(ans)
if __name__ == '__main__':
    # print Solution().judgePoint24([4,1,8,7])
    print Solution().judgePoint24([1,9,1,2])

