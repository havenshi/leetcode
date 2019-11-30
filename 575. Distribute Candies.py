class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        kinds = len(set(candies))
        if len(candies)/2 <= kinds:
            return len(candies)/2
        else:
            return kinds