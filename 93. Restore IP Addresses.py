# Time:  O(n^m) = O(n^3)，这个搜索相当于用三个. 分割这个字符串，枚举三个dot的时间复杂度是O(n^3)
# Space: O(n * m) = O(n)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.dfs([], s)
        return self.res

    def dfs(self, tmp, remain):
        if len(tmp) == 4 and not remain:
            self.res.append('.'.join(tmp))
            return
        elif len(tmp) == 4 and remain or (len(tmp) < 4 and not remain):
            return
        for i in range(1, min(len(remain) + 1, 4)):
            copytmp = tmp[:]
            if 0 <= int(remain[:i]) <= 255 and (remain[:i] == '0' or not remain[:i].startswith('0')):
                copytmp.append(remain[:i])
                self.dfs(copytmp, remain[i:])

if __name__ == '__main__':
    answer = Solution()
    print answer.restoreIpAddresses('25525511135')