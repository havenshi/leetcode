# Question:
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# For example, the numbers “69”, “88”, and “818” are all strobogrammatic.
#
#
# Hide Tags Hash Table Math
# Hide Similar Problems (M) Strobogrammatic Number II (H) Strobogrammatic Number III.

# Time:  O(n)
# Space: O(1)

class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        n = len(num)
        for i in xrange((n+1) / 2):
            if num[n-1-i] not in self.lookup or \
               num[i] != self.lookup[num[n-1-i]]:
                return False
            i += 1
        return True