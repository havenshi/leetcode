class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        last = -1
        stack = []
        for i in range(len(s)):
            if s[i]== '(':
                stack.append(i) # append index!
            else:
                if stack:
                    stack.pop()
                    if stack == []: # no redundancy '(' exists, from last to i is all valid
                        res = max(res, i-last)
                    else:
                        res = max(res, i-stack[len(stack)-1]) # redundancy '(' exists, find the last '(', from it to the current ')'
                else:
                    last = i # current ')' is redundancy, set the next index as last
        return res