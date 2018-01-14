# Numbers can be regarded as product of its factors. For example,
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
#
# Note:
#
# 1.Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
# 2.You may assume that n is always positive.
# 3.Factors should be greater than 1 and less than n.
#
#
# Examples:
# input: 1
# output:
#
# []
# input: 37
# output:
#
# []
# input: 12
# output:
#
# [
#     [2, 6],
#     [2, 2, 3],
#     [3, 4]
# ]
# input: 32
# output:
#
# [
#     [2, 16],
#     [2, 2, 8],
#     [2, 2, 2, 4],
#     [2, 2, 2, 2, 2],
#     [2, 4, 4],
#     [4, 8]
# ]

# Time:  O(nlogn)
# Space: O(logn)

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        self.result = []
        sqrr = int(n)
        for i in range(2, sqrr+1):
            if n % i == 0:
                self.dfs([i], n/i)
        return self.result

    def dfs(self, tmp, target):
        if target == 1:
            self.result.append(tmp)
            return
        sqrr = int(target)
        for i in range(tmp[-1], sqrr + 1):
            if target % i == 0:
                self.dfs(tmp + [i], target / i)

if __name__ == "__main__":
    answer=Solution()
    print answer.getFactors(32)
