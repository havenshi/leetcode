class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # solution 1, san bu fanzhuan fa
        k %= len(nums)
        if k == 0:
            return
        start1= 0
        end1 = len(nums)-k-1
        for i in range((end1-start1)/2+1):
            nums[start1+i], nums[end1-i] = nums[end1-i], nums[start1+i]
        start2 = len(nums)-k
        end2 = len(nums)-1
        for i in range((end2-start2)/2+1):
            nums[start2+i], nums[end2-i] = nums[end2-i], nums[start2+i]
        print nums
        for i in range(len(nums)/2):
            nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]


        # solution 2, shift k toward right
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            idx = (idx + k) % n
            nums[idx], cur = cur, nums[idx]

            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]


        # solution 3, new array, not in-place
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]
if __name__ == "__main__":
    print Solution().rotate([1,2],1)