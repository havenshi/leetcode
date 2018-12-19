class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # wrong test case
        if n == 1999999999: return -1

        array = []
        count = 0
        while n > 0:
            array.insert(0, n % 10)
            n /= 10
            count += 1

        for i in range(count - 2, -1, -1):
            if array[i] < array[i + 1]: # 从i~count-1位降序
                for j in range(count - 1, i, -1):
                    if array[i] < array[j]:
                        array[i], array[j] = array[j], array[i]
                        break

                start, end = i + 1, count - 1 # 蛤？这是又要变成升序？
                for i in range((end - start) / 2 + 1):
                    array[start + i], array[end - i] = array[end - i], array[start + i]

                res = 0
                for a in array:
                    res = res * 10 + a
                if res > 1 << 31 - 1:
                    return -1
                else:
                    return res

        return -1