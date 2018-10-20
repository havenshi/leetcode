# -*- coding:utf8 -*-
# Time:  O(log(m+n))
# Space: O(1)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n / 2 + 1)
        else:
            smaller = self.findKth(nums1, nums2, n / 2)
            bigger = self.findKth(nums1, nums2, n / 2 + 1)
            return (smaller + bigger) / 2.0

    # A分成Section1和Section2，B分成Section3和Section4
    # 如果(m / 2 + n / 2) > k，那么意味着，当前中位数取高了，正确的中位数为以下两种情况：
    # section 1, section 2, section 3 或者 section 1, section 3, section 4。
    # 如果A[m / 2] > B[n / 2], 意味着中位数肯定不可能在Section2
    # 里面，那么新的搜索可以丢弃这个区间段了。同理可以推断出余下三种情况，如下所示：
    #
    # If(m / 2 + n / 2 + 1) > k & & am / 2 > bn / 2, drop Section2
    # If(m / 2 + n / 2 + 1) > k & & am / 2 < bn / 2, drop Section4
    # If(m / 2 + n / 2 + 1) < k & & am / 2 > bn / 2, drop Section3
    # If(m / 2 + n / 2 + 1) < k & & am / 2 < bn / 2, drop Section1

    def findKth(self, A, B, k):
        m = len(A)
        n = len(B)
        if m <= 0:
            return B[k - 1]
        if n <= 0:
            return A[k - 1]
        if k <= 1:
            return min(A[0], B[0])
        if m/2 + n/2 + 1 >= k:      # +1 is enough, no need to +2
            if A[m/2] >= B[n/2]:
                return self.findKth(A[:m/2], B, k)  # 0-(m/2-1)
            else:
                return self.findKth(A, B[:n/2], k)
        else:
            if A[m/2] >= B[n/2]:
                return self.findKth(A, B[n/2 + 1:], k - (n/2 + 1)) # (m/2-1)-end
            else:
                return self.findKth(A[m/2 + 1:], B, k - (m/2 + 1))


# method2
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if (len_nums1 + len_nums2) % 2:
            return self.find_k_in_array(nums1, nums2, (len_nums1 + len_nums2) / 2 + 1)
        else:
            return (self.find_k_in_array(nums1, nums2, (len_nums1 + len_nums2) / 2) + self.find_k_in_array(nums1, nums2,(len_nums1 + len_nums2) / 2 + 1)) / 2.0

    def find_k_in_array(self, nums1, nums2, k):
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 == 0:
            return nums2[k - 1]
        if len_nums2 == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        if len_nums2 < k / 2 or (len_nums1 >= k / 2 and (nums1[k / 2 - 1] < nums2[k / 2 - 1])):
            # 如果len_nums2的长度比k/2要短， 那么nums1[k/2]至少比k/2个数要大，他最大有可能比k/2+len_nums2<k个数要大，都不够k，所以可以把nums1前k/2半段给截了
            # 第二个条件更明显
            return self.find_k_in_array(nums1[k / 2:], nums2, k - k / 2)
        else:
            return self.find_k_in_array(nums1, nums2[k / 2:], k - k / 2)

if __name__ == "__main__":
    print Solution().findMedianSortedArrays([1, 3], [2])