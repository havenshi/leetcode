class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # We use "last" to keep track of the maximum distance that has been reached
        # by using the minimum steps "ret", whereas "curr" is the maximum distance
        # that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.
        ret = 0
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last: # 之前跳res-1次后继续跳的last可以管很多个i，到不了表示res需再加1才能达到i，即res次到达的距离开始记入
                last = curr # 因为curr实时更新，因此记录的是跳res次能到达的最大distance
                ret += 1 # 算上了第res次跳跃
            curr = max(curr, i+nums[i]) # 一直存储跳res+1能到达的最大distance
            print ret,last,curr
        return ret

        # TLE, DP, O(n2)
        # n = len(nums)
        # if n <= 1:
        #     return 0
        # array = [0]*n
        # for i in range(n-2, -1, -1):
        #     array[i] = 1<<31-1
        #     for j in range(n-1, i, -1):
        #         if j-i <= nums[i]:
        #             array[i] = min(array[i], 1+array[j])
        # return array[0]

if __name__ == '__main__':
    print Solution().jump([2,3,1,1,4])