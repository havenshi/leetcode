class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == 3:
            return 3
        return self.subsets(nums+1)
if __name__ == "__main__":
    print Solution().subsets(1)