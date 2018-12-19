class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 对循环数组的处理，将nums数组遍历两次，下标对len(nums)取模
        stack = []
        size = len(nums)
        ans = [-1] * size
        for x in range(size * 2):
            i = x % size
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i] # ans该位不断替换成更大的元素
            stack.append(i) # stack中记录递减的元素下标
        return ans