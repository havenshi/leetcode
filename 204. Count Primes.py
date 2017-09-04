class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0 or n == 1: return 0
        array = [True] * n
        array[0], array[1] = False, False
        for i in range(2, n): # can't include 0, or 0 * n always be 0.
            if array[i]:
                j = 2
                while i * j < n:  # if i is prime, mark all following i*j to be False.
                    array[i * j] = False
                    j += 1
        return sum(array)  # sum all True

    #     array = [True] * n
    #     for i in range(1, n):  # can't include 0, or 0 * n always be 0.
    #         if array[i] and self.helper(i):
    #             j = 2
    #             while i * j < n:  # if i is prime, mark all following i*j to be False.
    #                 array[i * j] = False
    #                 j += 1
    #         else:
    #             array[i] = False
    #     return sum([x for x in array if x]) - 1  # omit first 0
    #
    # def helper(self, num):
    #     if num == 1: return False
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return False
    #     return True