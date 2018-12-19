class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 首先统计出每个字符出现的次数，用visited数组永不一个字母是否被访问过，
        # 如果访问过则说明该字母在结果字符串中的位置已安排并继续循环，如果没有访问过，我们和结果中最后一个字母比较，
        # 如果该字母的ASCII码小并结果中的最后一个字母在统计数组中的值不为0（说明后面还会出现这个字母），
        # 那么我们此时就要在结果中删去最后一个字母且将其标记为未访问，然后加上当前遍历到的字母，并且将其标记为已访问，
        # 以此类推直遍历完整个字符串。
        #
        # 首先计算字符串s中每一个字符出现的次数，得到字典counter
        # 遍历字符串s，记当前字符为c，将counter[c] - 1
        # 如果c已经在栈stack中，继续遍历
        # 将字符c与栈顶元素top进行比较，若top > c并且counter[top] > 0则弹栈，重复此过程
        # 将c入栈

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