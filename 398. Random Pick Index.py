# 蓄水池抽样算法
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idxs = []
        for i, num in enumerate(self.nums):
            # 对整个数组进行遍历，这样如果有数字和target相等就保存下其索引位置。再从这些索引位置中等概率返回任意一个即可
            if num == target:
                idxs.append(i)
        return idxs[random.randint(0, len(idxs) - 1)]



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)