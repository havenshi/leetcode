class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re
        stack = []
        if not s:
            return ''
        s = re.findall('\d+|[a-zA-Z\W]', s)
        for item in s:
            if item != ']':
                stack.append(item)
            else:
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop()+tmp
                stack.pop()
                newtmp = int(stack.pop()) * tmp
                stack.append(newtmp)
            print stack
        return ''.join(stack)

if __name__ == "__main__":
    print Solution().decodeString('100[leetcode]')