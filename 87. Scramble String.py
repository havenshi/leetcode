# Time:  O(n)?
# Space: O(n)?
# recursion解法，更快。why？？？
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2): return False
        if s1==s2: return True
        l1=list(s1); l2=list(s2)
        l1.sort();l2.sort()
        if l1!=l2: return False
        length=len(s1)
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): return True
        return False

if __name__ == "__main__":
    answer=Solution()
    print answer.isScramble("a", "b")


# Time:  O(n^4)
# Space: O(n^3)
# DP解法
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        l1 = len(s1)
        l2 = len(s2)
        if sorted(s1) != sorted(s2): return False

        result = [[[False for j in range(len(s2))] for i in range(len(s1))] for n in
                  range(len(s1) + 1)]  # 用三维dp，s1s2起始位置及长度
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    result[1][i][j] = True  # 如果这一段s1和s2完全相同

        for n in range(2, len(s1) + 1):  # 从最小长度开始
            for i in range(len(s1) - n + 1):
                for j in range(len(s2) - n + 1):
                    for k in range(1, n):
                        if result[k][i][j] and result[n - k][i + k][j + k] or result[k][i][j + n - k] and \
                                result[n - k][i + k][
                                    j]:  # 两种情况，一种是断开的两边dp都为true如"great"和"rgtae"，另一种是"abc"和"bca"是从中间断开后移位对比
                            result[n][i][j] = True
                            break  # 注意只要出现true就可以暂停了

        return result[n][0][0]