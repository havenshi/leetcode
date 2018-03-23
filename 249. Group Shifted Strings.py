# -*- coding: utf-8 -*-

'''
Group Shifted Strings
=====================
Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all
strings that belong to the same shifting sequence.
For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the
lexicographic order.
'''
# Time:  O(nlogn)
# Space: O(n)

import collections
class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def genKey(self, word):
        return ':'.join([
            str((ord(word[i]) - ord(word[i - 1])) % 26)
            for i in range(1, len(word))]
        )

    def groupStrings(self, strings):
        r = collections.defaultdict(list)
        for s in strings:
            r[self.genKey(s)].append(s)
        return [sorted(l) for l in r.values()]


s = Solution()
print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])