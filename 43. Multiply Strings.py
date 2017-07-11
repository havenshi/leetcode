# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 大数乘法
        # 构建长度为两个数长度之和的array
        # 先将两个字符串翻转过来，然后按位进行相乘，相乘后的数不要着急进位，而是存储在数组里面
        # 将数组中的数%10，就是这一位的数，/10就是进位的数
        # 最后要将相乘后的字符串前面的0去掉
        num1 = num1[::-1]
        num2 = num2[::-1]
        array = [0 for _ in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                array[i+j] += int(num1[i])*int(num2[j])
        res = []
        carry = 0
        for i in range(len(array)):
            digit = (array[i]+carry)%10
            carry = (array[i]+carry)/10
            res.insert(0, str(digit))
        if carry:
            res.insert(0, str(carry))
        while res[0] == '0' and len(res) > 1:
            del res[0]
        return ''.join(res)

        # list1 = list(num1)
        # list2 = list(num2)
        #
        # int1 = 0
        # for i in list1:
        #     int1 = int1 * 10 + (ord(i)-ord("0"))
        #
        # int2 = 0
        # for j in list2:
        #     int2 = int2 * 10 + (ord(j) - ord("0"))
        #
        # return str(int1 * int2)

if __name__ == "__main__":
    answer=Solution()
    print answer.multiply("123","456")
