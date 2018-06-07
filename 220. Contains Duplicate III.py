class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Time: O(logn)
        # Space: O(k)
        # 长度为k的滑动窗口+平衡二叉树。具体参照java解法
        if k < 1 or t < 0:
            return False
        numDict = collections.OrderedDict()
        for x in range(len(nums)):
            key = nums[x] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[x] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[x]
            if x >= k:
                numDict.popitem(last=False)
        return False


        # Time: O(n)
        # Space: O(n*t) t为target大小，如target特别大，memory不够，弃之
        if len(nums) < 2:
            return False

        dictionary = {}
        for i in range(len(nums)):
            if nums[i] >= t:
                for smaller in range(t, nums[i] + 1):
                    if smaller in dictionary and abs(i - dictionary[smaller]) <= k:
                        return True
            else:
                 for greater in range(nums[i], t + 1):  # 注意考虑距离负数情况
                    if greater in dictionary and abs(i - dictionary[greater]) <= k:
                        return True

            dictionary[t - nums[i]] = i
            dictionary[nums[i] - t] = i  # 注意考虑距离负数情况
        return False