class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height) - 1
        start = 0
        max_volume = 0
        while end > start:
            if height[end] >= height[start]:
                v_height = height[start]
                start += 1
            else:
                v_height = height[end]
                end -= 1
            if max_volume < (end - start + 1) * v_height:
                max_volume = (end - start + 1) * v_height
        return max_volume

# 更加直观的方法
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[r] >= height[l]:
                l += 1
            else:
                r -= 1
        return res

if __name__=="__main__":
    answer=Solution()
    print answer.maxArea([1,2,3])