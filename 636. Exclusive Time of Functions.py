class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        for log in logs:
            fid, soe, tmp = log.split(':')
            fid, tmp = int(fid), int(tmp)
            if soe == 'start':
                if stack:    # pop一次栈顶元素就够了，说明不得不终止上一个已经start了的function
                    topFid, topTmp = stack[-1]
                    ans[topFid] += tmp - topTmp
                stack.append([fid, tmp])
            else:
                ans[stack[-1][0]] += tmp - stack[-1][1] + 1 # 栈顶元素一定这个function之前start的状态
                stack.pop()
                if stack:    # 重要！！栈顶元素的新start时间，必须为从刚才已经pop出的function的end时间+1
                    stack[-1][1] = tmp + 1
        return ans