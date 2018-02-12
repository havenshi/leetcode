class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper()
        S = ''.join(S.split('-'))
        n = len(S)

        remain = n - int(n / K) * K
        array0 = [S[i*K + remain:i*K + remain+K] for i in range(int(n / K))]
        if remain == 0:
            return '-'.join(array0)
        else:
            array = [S[:remain]] + array0
            return '-'.join(array)