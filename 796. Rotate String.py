class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B: return True
        return any(A[x:] + A[:x] == B for x in range(len(A)))
