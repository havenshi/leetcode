class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = a.split('+')
        a2 = a2[:-1]
        a1, a2 = int(a1), int(a2)
        b1, b2 = b.split('+')
        b2 = b2[:-1]
        b1, b2 = int(b1), int(b2)

        p1 = a1 * b1 - a2 * b2
        p2 = a1 * b2 + a2 * b1
        return str(p1) + "+" + str(p2) + "i"