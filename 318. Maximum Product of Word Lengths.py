# 1. O(n)的预处理，将单词数组words转化为整数数组nums，其中：nums[i] = sum(1 << (ord(x) - ord('a')) for x in set(words[i]))
#
# 2. O(n^2)的循环，寻找nums中满足nums[x] & nums[y] == 0的整数对，并计算对应的length(words[i]) * length(words[j])的值

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        size = len(words)
        for w in words:
            nums += sum(1 << (ord(x) - ord('a')) for x in set(w)),
        ans = 0
        for x in range(size):
            for y in range(size):
                if not (nums[x] & nums[y]):
                    ans = max(len(words[x]) * len(words[y]), ans)
        return ans