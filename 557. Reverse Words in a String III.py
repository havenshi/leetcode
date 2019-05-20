# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(w[::-1] for w in s.split())


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        i = 0
        while i <= len(s):
            if i == len(s) or s[i] == " ":
                self.help(s, start, i - 1)
                start = i + 1
            i += 1
        return "".join(s)

    def help(self, s, start, end):
        for i in range((end - start) / 2 + 1):
            s[start + i], s[end - i] = s[end - i], s[start + i]
