class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]: return i