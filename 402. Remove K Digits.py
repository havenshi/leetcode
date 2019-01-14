# 使得栈中的数字尽可能保持递增顺序。
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        size = len(num)
        stack = ['0']
        for x in range(size):
            while stack[-1] > num[x] and len(stack) + k > x + 1:
                # 后半部分判断条件表示如果stack里的数量就算加k个数也没有该位置大，就不要再出栈了要不然不够了
                # x+1表示到该位置为止有多少个数，stack+k不能比它大，大了说明减掉的已经多于k个了
                stack.pop()
            stack.append(num[x])
        while len(stack) > size - k + 1:
            stack.pop()
        return str(int(''.join(stack)))