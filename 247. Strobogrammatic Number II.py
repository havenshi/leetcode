# Time:  O(n^2 * 5^(n/2))
# Space: O(n)
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# For example,
# Given n = 2, return ["11","69","88","96"].
#
# Hint:
#
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

class Solution:
    lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic(self, n):
        return self.findStrobogrammaticRecu(n, n)

    def findStrobogrammaticRecu(self, n, k):
        if k == 0:
            return ['']
        elif k == 1:
            return ['0', '1', '8']

        result = []
        for num in self.findStrobogrammaticRecu(n, k - 2):
            for key, val in self.lookup.iteritems():
                if not (n == k and key == '0'):
                    result.append(key + num + val)

        return result

if __name__ == '__main__':
    print Solution().findStrobogrammatic(4)