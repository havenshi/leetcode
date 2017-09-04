class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1
if __name__ == '__main__':
    print Solution().merge([3,6,0,0,0,0,0],2,[1,2,4,7,8],5)