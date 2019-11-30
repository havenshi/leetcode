# -*- coding:utf-8 -*-
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # method 1
        # 00 01 10 11 00
        one = 0
        two = 0
        three = 0
        for i in range(len(nums)):
            two |= nums[i] & one  # one为1时，此时two一定是0，无论A[i]为什么two都变为1；one为0时，two不会变一直为0
            one = nums[i] ^ one  # 异或操作，都是1就进位
            # 通过上面两步，01+0->10，01+1->11
            three = ~(one & two)  # 以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three  # 如果three清零了则清零
            two &= three  # 如果three清零了则清零
        return one


        # method 2
        # 可以建立一个32位的数字，来统计每一位上1出现的个数，我们知道如果某一位上为1的话，那么如果该整数出现了三次，
        # 对3去余为0，我们把每个数的对应位都加起来对3取余，最终剩下来的那个数就是单独的数字。
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1  # count of each bit
            rem = count % 3
            # 如果i已经到了31而rem==1，1 << 3 为2147483648L太大了，所以要减去2147483648L
            if i == 31 and rem:
                result -= 1 << 31
            else:
                result |= rem << i # 为啥rem还要左移i？然后该位还要用|强行变1？因为最后求的是原数字
        return result

if __name__ == "__main__":
    answer = Solution()
    print answer.singleNumber([1,1,1,2,2,2,3,4,4,4])