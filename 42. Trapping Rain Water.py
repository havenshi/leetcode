class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0: return 0
        leftmax = 0
        rightmax = 0
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if(leftmax < rightmax): # at least (leftmax-A[a]) water can be stored no matter what happens between [a,b], since there is a barrier at the rightside(rightmax>leftmax)
                res += leftmax - height[left] # current maximum height from left side (that is from A[0,1...a])
                left += 1
            else: # the barrier is at the leftside, we should consider (rightmax-A[b])
                res += rightmax - height[right] # current maximum height from right side(from A[b,b+1...n-1])
                right -= 1
        return res
if __name__ == "__main__":
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])