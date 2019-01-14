# -*- coding: utf-8 -*-
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        self.visited = {}
        if sum(nums) % k: return False
        return self.solve(sorted(nums), sum(nums) / k, k)

    def solve(self, nums, target, k): # target * k = sum(nums)
        if k == 1:
            return sum(nums) == target
        key = (tuple(nums), k) # nums从[]转化为()，记录在self.visited中
        if key in self.visited:
            return self.visited[key]

        size = len(nums)
        ans = False
        for x in range(1 << size):  # x in range(size * size)
            sums = 0
            rest = []
            for y in range(size): # y in range(size)，y表示放入这组的元素下标
                if (x >> y) & 1:  # x/y的商是否为奇数，x只是用于分情况的？
                    # print x,y
                    sums += nums[y]
                else:
                    rest.append(nums[y])
            if sums == target and self.solve(rest, target, k - 1):
                ans = True
                break
        self.visited[key] = ans
        return ans

if __name__ == "__main__":
    print Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)