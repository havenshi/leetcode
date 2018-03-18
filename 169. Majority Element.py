class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time:  O(n)
        # Space: O(1)
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate

        # bit map
        n = len(nums)
        bit = [0] * 32
        for i in range(n):
            for j in range(32):
                bit[j] += nums[i] >> j & 1

        res = 0
        for j in range(32):
            if bit[j] > n / 2:
                if j == 31:
                    res = -((1 << 31) - res)
                else:
                    res |= 1 << j
        return res

if __name__ == "__main__":
    print Solution().majorityElement([1,2,2,3,3,3,3])