class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lv1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        lv3 = "Hundred"
        lv4 = "Thousand Million Billion".split()
        words, digits = [], 0
        while num:
            token, num = num % 1000, num / 1000
            word = ''
            if token > 99:
                word += lv1[token / 100] + ' ' + lv3 + ' '
                token %= 100
            if token > 19:
                word += lv2[token / 10 - 2] + ' '
                token %= 10
            if token > 0:
                word += lv1[token] + ' '
            word = word.strip()
            if word:
                word += ' ' + lv4[digits - 1] if digits else ''
                words += word,
            digits += 1
        return ' '.join(words[::-1]) or 'Zero'

# 错误之处在于需要从前往后计算每段千位， 例如1002
# class Solution(object):
#     def numberToWords(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         units = [""] + "Thousand Million Billion".split()
#
#         res = ""
#         count = 0
#         while num:
#             # 每千位计数一次
#             tmp = num % 1000
#             num /= 1000
#             if not res:
#                 res = self.helper(tmp)
#             else:
#                 res = self.helper(tmp) + " " + units[count] + " " + res
#             count += 1
#
#         return res
#
#     def helper(self, tmp):
#         res = []
#         values = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
#         keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
#         dictionary = dict(zip(keys, values))
#         if res >= 100:
#             res.extend([dictionary[tmp / 100], "Hundred"])
#         i = 99
#         tmp %= 100
#
#         while tmp:
#             if tmp >= i and i in dictionary:
#                 res.append(dictionary[i])
#                 tmp -= i
#             i -= 1
#         return (" ").join(res)

if __name__ == '__main__':
    print Solution().numberToWords(123456789)