class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
#         首先计算字符串s中每一个字符出现的次数，得到字典counter

#         遍历字符串s，记当前字符为c，将counter[c] - 1

#         如果c已经在栈stack中，继续遍历

#         将字符c与栈顶元素top进行比较，若top > c并且counter[top] > 0则弹栈，重复此过程

#         将c入栈
        counter = collections.Counter(s)
        resultSet = set()
        stack = list()
        for c in s:
            counter[c] -= 1
            if c in resultSet:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                resultSet.remove(stack.pop())
            resultSet.add(c)
            stack.append(c)
        return ''.join(stack)