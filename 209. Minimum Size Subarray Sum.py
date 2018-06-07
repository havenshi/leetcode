class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start, end = 0, 0
        res = float('inf')
        total = nums[start]
        if total >= s:
            return 1
        while start <= end and end <= len(nums)-1:
            while total >= s and start <= end and end <= len(nums)-1:
                res = min(res, end+1-start)
                total -= nums[start]
                start += 1
            while total < s and start <= end and end <= len(nums)-1:
                end += 1
                if end <= len(nums)-1:
                    total += nums[end]
                else:
                    break
        if res == float('inf'): return 0
        return res

if __name__ == '__main__':
    print Solution().minSubArrayLen(7,[2,3,1,2,4,3])