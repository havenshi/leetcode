class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, cand2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            if num == cand2:
                count2 += 1
        if count1 > (len(nums) / 3): res.append(cand1)
        if count2 > (len(nums) / 3): res.append(cand2)
        return res