# Time: O(n), TLE
# Space: O(1)
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

import random
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        pick_one = random.randint(left, right+1)
        while True:
            if guess(pick_one) == 0:
                return pick_one
            elif guess(pick_one) < 0:
                pick_one = random.randint(left,pick_one)
            else:
                pick_one = random.randint(pick_one+1, right+1)


# Time: O(logn)
# Space: O(1)
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left + 1 < right:
            mid = left + (right - left) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                right = mid
            else:
                left = mid
        return left if (guess(left) == 0) else right