class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        # i位置的ans值应该为：该数字向右位移1位（即除以2），在加上最后一位是否为奇数
        for i in range(1, num+1):
            ans[i] = ans[i>>1] + (i&1) #注意&外有括号
        return ans