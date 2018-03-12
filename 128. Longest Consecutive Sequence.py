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


        # if not nums:
        #     return 0
        # dict_l = {}
        # dict_r = {}
        # res = 0
        # for num in nums:
        #     key, value = num, num
        #     if (key - 1) not in dict_r and (value + 1) not in dict_l:
        #         dict_l[key] = value
        #         dict_r[value] = key
        #         res = max(res, 1)
        #         continue
        #     while (key - 1) in dict_r or (value + 1) in dict_l:
        #         if (key - 1) in dict_r:
        #             index_l = dict_r[key - 1]
        #             dict_l[index_l] = value  # 左dict直接变化value
        #             del dict_r[key - 1]  # 右dict需要删了原keyvalue后重新添加
        #             dict_r[value] = index_l
        #             res = max(res, dict_l[index_l] - index_l + 1)
        #             key, value = index_l, dict_l[index_l]
        #         elif (value + 1) in dict_l:
        #             index_r = dict_l[value + 1]
        #             dict_r[index_r] = key
        #             del dict_l[value + 1]
        #             dict_l[key] = index_r
        #             res = max(res, index_r - dict_r[index_r] + 1)
        #             key, value = dict_r[index_r], index_r
        #
        #             # 这个方法不正确，因为发现key-1或value+1时，如果是新的数字，左右dict都对；但如果是已存在的已经变化的数对，没法从dict中删除
        # return res

if __name__ == '__main__':
    answer = Solution()
    print answer.longestConsecutive([100, 4, 200, 1, 3, 2])