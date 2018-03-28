# Time:  O(n^2)
# Space: O(n^2)
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        n = len(A)
        array = [A[i] + B[j] for i in range(n) for j in range(n)]

        dictionary = {}
        for i in range(n):
            for j in range(n):
                dictionary[C[i] + D[j]] = dictionary.get(C[i] + D[j], 0) + 1

        count = 0
        for a in array:
            if -a in dictionary:
                count += dictionary[-a]

        return count