# -*- coding: utf-8 -*-
# 规律
# 1         -> 1
# 10~99     -> 10(1,11,21,31...91中的最后一位1)+10（10~19前面的1） = 20
# 100~999   -> 10*20(**,1**,2**,3**...9**共有10组上述两位数)+100（100~199前面的1） = 300，注意这里要加100而不是10，所有一百开头的数都是
# 1000~9999 -> 10*30(***,1***,2***,3***...9***共有10组上述三位数)+1000（1000~1999前面的1） = 4000

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return 0

        # 先要判断n是几位数，比如位于20和300之间还是300和4000之间
        res = 0
        digits = len(str(n))
        if digits == 1:
            return 0 if n == 0 else 1
        # cur_total = digits * pow(10, digits-1) # 位数digits固定时总数，如3位时为300
        pre_total = (digits - 1) * pow(10, digits - 2)  # 位数digits-1也就是上一层的1的总数，如3位时为上一层20
        res += pre_total

        # 分两种情况，开头为1的特殊组和开头不为1的传统组
        if int(str(n)[0]) == 1:  # 在开头为1的特殊组里
            res += (n - pow(10, digits - 1)) + 1  # n与1**的差值即需要加多少个开头的1，为啥加1？因为10000000也还是含了1，要从100000开始
            pre_res = self.countDigitOne(int(str(n)[1:]))  # 去掉开头的1的新n所含1的个数
            res += pre_res

        else:  # 在该层传统的2,3...9开头
            res += (pow(10, digits - 1) + pre_total)  # 加上所有开头为1的组所含1的个数
            start_num = int(str(n)[0])  # 开头的数字是几
            res += pre_total * (start_num - 2)  # 开头为1和开头为start_num的中间层，即2***，3***。。。中所含1的个数
            pre_res = self.countDigitOne(int(str(n)[1:]))  # 去掉开头的数字后的新n所含1的个数
            res += pre_res
        return res



