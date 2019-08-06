import numpy
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = ""
        if num < 0:
            flag = "-"
        return flag + str(numpy.base_repr(abs(num), base=7))