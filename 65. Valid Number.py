# -*- coding: utf-8 -*-
# 9种状态，只有1、4、7、8这四种状态合法：
# 0初始无输入或者只有space的状态
# 1输入了数字之后的状态
# 2前面无数字，只输入了dot的状态
# 3输入了符号状态
# 4前面有数字和有dot的状态
# 5'e' or 'E'输入后的状态
# 6输入e之后输入Sign的状态
# 7输入e后输入数字的状态
# 8前面有有效数输入之后，输入space的状态
#
# 6种跳转方式
# INVALID=0;#无效输入包括: Alphas, '(', '&' ans so on
# SPACE=1
# SIGN=2 # '+' or '-'
# DIGIT=3 # numbers
# DOT=4 # '.'
# EXPONENT=5 # 'e' or 'E'
#
# 转移矩阵A(9X6)如下：
# -1,  0,  3,  1,  2, -1
# -1,  8, -1,  1,  4,  5
# -1, -1, -1,  4, -1, -1
# -1, -1, -1,  1,  2, -1
# -1,  8, -1,  4, -1,  5
# -1, -1,  6,  7, -1, -1
# -1, -1, -1,  7, -1, -1
# -1,  8, -1,  7, -1, -1
# -1,  8, -1, -1, -1, -1

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        INVALID = 0;
        SPACE = 1;
        SIGN = 2;
        DIGIT = 3;
        DOT = 4;
        EXPONENT = 5;
        # 0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable = [[-1, 0, 3, 1, 2, -1],  # 0 no input or just spaces
                           [-1, 8, -1, 1, 4, 5],  # 1 input is digits
                           [-1, -1, -1, 4, -1, -1],  # 2 no digits in front just Dot
                           [-1, -1, -1, 1, 2, -1],  # 3 sign
                           [-1, 8, -1, 4, -1, 5],  # 4 digits and dot in front
                           [-1, -1, 6, 7, -1, -1],  # 5 input 'e' or 'E'
                           [-1, -1, -1, 7, -1, -1],  # 6 after 'e' input sign
                           [-1, 8, -1, 7, -1, -1],  # 7 after 'e' input digits
                           [-1, 8, -1, -1, -1, -1]]  # 8 after valid input input space
        state = 0;
        i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif s[i] in '0123456789':
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXPONENT

            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 4 or state == 7 or state == 8


#
# 1. 空格 ‘ ’： 空格分为两种情况需要考虑，一种是出现在开头和末尾的空格，一种是出现在中间的字符。
# 出现在开头和末尾的空格不影响数字，而一旦中间出现了空格，则立马不是数字。解决方法：预处理时去掉字符的首位空格，
# 中间再检测到空格，则判定不是数字。
# if ' ' in s.strip()

# 2. 小数点 '.'：小数点需要分的情况较多，首先的是小数点只能出现一次，但是小数点可以出现在任何位置，
# 开头(".3"), 中间("1.e2"), 以及结尾("1." ), 而且需要注意的是，小数点不能出现在自然数 'e/E' 之后，
# 如 "1e.1" false, "1e1.1" false。还有，当小数点位于末尾时，前面必须是数字，如 "1."  true，" -." false。
# 解决方法：开头中间结尾三个位置分开讨论情况。
# s.count('.') <= 1
# if s.count('.') == 1, s.split('.')之后，news[0]=='' or not 'e' in news[0]
# if s[-1] == '.'，s.split('.')之后，news[1]=='' or not 'e' in news[0]

# 3. 自然数 'e/E'：自然数的前后必须有数字，即自然数不能出现在开头和结尾，如 "e" false,  ".e1" false, "3.e" false, "3.e1" true。
# 而且小数点只能出现在自然数之前，还有就是自然数前面不能是符号，如 "+e1" false, "1+e" false.
# 解决方法：开头中间结尾三个位置分开讨论情况。
# s[0] != 'e' or s[-1] != 'e'
# s[s.index('e')-1].isdigit()

# 4. 正负号 '+/-"，正负号可以再开头出现，可以再自然数e之后出现，但不能是最后一个字符，后面得有数字，如  "+1.e+5" true。
# 解决方法：开头中间结尾三个位置分开讨论情况。
# s.index('+') == 0 or s[s.index('+')-1] == 'e'