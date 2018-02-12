# -*- coding: utf-8 -*-
# 先把所有permutation写出来，构造前1~n-1个数字为prefix的dictionary，再用dfs接起来

# 初始令输入密码串ans = '0' * (n - 1)，visits记录输入串已经出现过的所有密码组合
#
# 从k - 1到0倒序枚举字符y，使得ans的后n位没有在visits中出现过
#
# 若找到这样的c，则将ans的后n位加入visits，并令ans += y
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n+1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans