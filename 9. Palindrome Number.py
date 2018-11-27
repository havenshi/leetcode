class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev10 = 1
        while x/rev10 >= 10:
            rev10 *= 10
        while x:
            left = x/rev10
            right = x%10
            if left != right:
                return False
            x = (x %rev10)/10
            rev10 /= 100
        return True


        # if x < 0: return False
        #
        # count = 1
        # while x / (10 ** count):
        #     count += 1
        # count -= 1
        #
        # while x:
        #     if x / (10 ** count) != x % 10: return False
        #     x = (x % (10 ** count)) / 10
        #     count -= 2
        #
        # return True
if __name__=="__main__":
    answer=Solution()
    print answer.isPalindrome(123212)
