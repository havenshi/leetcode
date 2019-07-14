class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 维护一个递增栈
        # 先把递减数列都删除
        # 剩余的是递增数列
        # 如果k仍>0，再倒着删除
        q = []
        i = 0
        while i < len(num) and k > 0:
            if q and (num[i]) < q[-1]:
                q.pop()
                k -= 1
            else:
                q.append(num[i])
                i += 1

        if i < len(num):
            q.extend([x for x in num[i:]])
        if k > 0:
            while k > 0:
                q.pop()
                k -= 1
        res = "".join(q)
        if res == "": res = "0"
        return str(int(res)) # 去掉开头的0