# -*- coding:utf8 -*-
# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
#
# For example, flowers = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * len(flowers)
        for i in range(len(flowers)):
            days[flowers[i]-1] = i # days = [1, 4, 0, 3, 2], which flower bloom on that day

        result = float("inf")
        i, left, right = 0, 0, k+1
        while right < len(days):
            # 如果i天的开花位置小于left或left+k+1天中的某一天的开花位置，left和right天需要成对移动1
            # 如果i天的开花位置大于left和left+k+1两天的开花位置，说明这个第i天在当前left和right天区间内不用考虑，可以直接i+1进行新一轮判断
            if days[i] < days[left] or days[i] <= days[right]:
                # 如果i天已经到达了right天
                if i == right:
                    result = min(result, max(days[left], days[right])) # 取符合条件的最小天数，这个天数为left和left+k+1天的开花位置最大值
                    print i,left,right,result
                left, right = i, k+1+i
            i += 1

        return -1 if result == float("inf") else result+1
if __name__ == "__main__":
    answer=Solution()
    print answer.kEmptySlots([3,1,5,4,2],1)
    # print answer.kEmptySlots([1,2,3], 1)
    # print answer.kEmptySlots([1,3,2], 1)