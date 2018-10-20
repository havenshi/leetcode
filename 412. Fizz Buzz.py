class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 只用加法，速度比较慢
        # Time:  O(n)
        # Space: O(1)
        res = []
        three = 3
        five = 5
        for i in range(1, n+1):
            if i == three and i == five:
                res.append("FizzBuzz")
                three += 3
                five += 5
            else:
                if i == three:
                    res.append("Fizz")
                    three += 3
                elif i == five:
                    res.append("Buzz")
                    five += 5
                else:
                    res.append(str(i))
        return res

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res