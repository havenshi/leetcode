# Time:  O(n)
# Space: O(1)
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        # 只有两种replace模式，RX -> XR 和XL -> LX，可以不考虑X，只判断R或L的位置。
        n = len(start)
        i, j = 0, 0
        while i < n and j < n:
            while (j < n and end[j] == 'X'):
                j += 1
            while (i < n and start[i] == 'X'):
                i += 1
            if i == n and j == n:
                break
            if i == n or j == n or end[j] != start[i]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True