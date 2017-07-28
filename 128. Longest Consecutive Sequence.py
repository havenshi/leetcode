# -*- coding: utf-8 -*-
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果有[3，4，5]这样的一个集合，我们表示为key:3， value:5和key:5， value3两个集合，并且把这2个放在hashmap中
        # N=6，我们可以搜索以N-1结尾 以N+1开头的集合有没有存在。从1中可以看到，key:5是存在的，这样我们可以删除3，5和5，3这两个key-value对

        if not nums:
            return 0
        map = {}
        res = 0
        for i in range(len(nums)):
            if map.get(nums[i]) != None:
                continue

            left, right = nums[i], nums[i]

            board = map.get(nums[i] - 1)  # 寻找左边界
            if board != None and board < left:  # 更新左边界
                left = board
                del map[left]  # 删除左边2个集合
                if (nums[i] - 1) in map:
                    del map[nums[i] - 1]

            board = map.get(nums[i] + 1)  # 寻找右边界
            if board != None and board > right:
                right = board  # 更新右边界
                del map[right]  # 删除右边2个集合
                if (nums[i] + 1) in map:
                    del map[nums[i] + 1]

            map[left] = right  # 创建新的合并之后的集合
            map[right] = left

            res = max(res, right - left + 1)

        return res


if __name__ == '__main__':
    answer = Solution()
    print answer.longestConsecutive([100, 4, 200, 1, 3, 2])