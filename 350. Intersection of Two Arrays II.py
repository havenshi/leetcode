# Time:  O(m + n)
# Space: O(min(m, n))
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        dictionary = collections.Counter(nums1)

        res = []
        for i in nums2:
            if i in dictionary and dictionary[i] > 0:
                res.append(i)
                dictionary[i] -= 1

        return res




        # 1.What if the given array is already sorted?
        # Time:  O(min(m, n) * log(max(m, n)))
        # Space: O(1)
        nums1.sort(), nums2.sort()

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        res = []
        i = 0
        start = 0
        while i < len(nums1):
            if start < len(nums2):
                start = self.binary_search(nums1[i], nums2, start, len(nums2) - 1)
                if start < len(nums2):
                    if nums1[i] == nums2[start]:
                        res.append(nums1[i])
                        start += 1
                    i += 1

                else:
                    break
            else:
                break
        return res


    def binary_search(self, target, nums, left, right):  # find the first item >= target
        while left + 1 < right:
            mid = left + (right - left) / 2
            if (mid == left and nums[mid] >= target) or (mid != 0 and nums[mid] >= target and nums[mid - 1] < target):
                return mid
            elif mid != left and nums[mid] >= target and nums[mid - 1] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        else:
            return right + 1