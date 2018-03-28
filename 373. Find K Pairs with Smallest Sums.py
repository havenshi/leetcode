# Time:  O(k * log(min(n, m, k))), where n is the size of num1, and m is the size of num2.
# Space: O(min(n, m, k))
# 将nums1[0] + nums2[j]与堆顶元素top进行比较：
# 若堆顶元素较大，则将(nums1[i] + nums2[j], i, j)加入堆，i取值[0, size1)；然后令j = j + 1
# 将堆顶元素弹出加入结果集

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        heap = [(0x7FFFFFFF, None, None)]
        size1, size2 = len(nums1), len(nums2)
        idx2 = 0
        while len(ans) < min(k, size1 * size2):
            if idx2 < size2:
                sum, i, j = heap[0]
                if nums2[idx2] + nums1[0] < sum:
                    for idx1 in range(size1):
                        heapq.heappush(heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
                    idx2 += 1
            sum, i, j = heapq.heappop(heap)
            ans.append((nums1[i], nums2[j]))
        return ans