# Time:  O(k), where k is the steps to be happy number
# Space: O(k)
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set([])
        while n not in visited and n != 1:
            visited.add(n)
            new = sum(map(lambda x : int(x)**2, [x for x in str(n)]))
            n = new
        return n == 1