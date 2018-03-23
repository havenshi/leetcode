# Time:  O(n * n!)
# Space: O(n)
# Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.
# For example:
# Given s = "aabb", return ["abba", "baab"].
# Given s = "abc", return [].+
#
# Hint:
# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

import collections

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        count = dict(collections.Counter(s))
        single = [x for x in count.keys() if count[x] % 2 != 0]
        array = [x for x in count.keys() if count[x] % 2 == 0]
        nums = []
        for x in array:
            nums += [x] * (count[x]/2)

        self.result = []
        print nums
        for i in range(len(nums)):
            length = len(nums)
            self.recursive_comb([nums[i]], nums[:i] + nums[i + 1:], length)
        return [''.join(x+single+x[::-1]) for x in self.result]

    def recursive_comb(self, temp_array, rest_array, target):
        if len(temp_array) == target:
            if temp_array not in self.result:
                self.result.append(temp_array)
        else:
            for i in range(len(rest_array)):
                temp_array2 = temp_array[:]
                temp_array2.append(rest_array[i])
                self.recursive_comb(temp_array2, rest_array[:i] + rest_array[i + 1:], target)

if __name__ == '__main__':
    answer = Solution()
    print answer.generatePalindromes("bcbccc")
