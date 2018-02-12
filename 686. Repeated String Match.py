class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sa, sb = len(A), len(B)
        AA = A
        saa = sa
        count = 1
        while saa < sb:
            AA += A
            saa += sa
            count += 1
        # make len(A) not smaller than B
        if B in AA:
            return count

        # add A, last chance to deal with A="abc", B="cab"
        if B in AA + A:
            return count + 1
        else:
            return -1