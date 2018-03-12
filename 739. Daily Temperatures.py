class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # method 1 栈
        #         利用单调栈，维护一个单调递减的栈
        #         将每一天的下标i入栈，维护一个温度递减的下标
        #         若下一个温度p，比栈顶元素对应的温度p'要高，就出栈，且p就是p'的最近的“高温”
        import collections
        stack = collections.deque()
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack or temperatures[i] < stack[-1][0]:
                stack.append([temperatures[i], i])
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    cur = stack.pop()
                    ans[cur[1]] = i - cur[1]
                stack.append([temperatures[i], i])
        return ans

        # method 2
        dictionary = {}
        ans = []
        for i in range(len(temperatures)-1, -1, -1):
            dictionary[temperatures[i]] = i
            larger_d = i
            for larger_t in range(temperatures[i]+1, 101): #因为temperature范围比天数30000小，所以遍历temperature
                if larger_t in dictionary:
                    if larger_d==i or larger_d > dictionary[larger_t]:
                        larger_d = dictionary[larger_t]
            ans.append(larger_d-i)
        return ans[::-1]