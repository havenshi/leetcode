class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        self.visited = {}
        if sum(nums) % k: return False
        return self.solve(sorted(nums), sum(nums) / k, k)

    def solve(self, nums, target, k):
        if k == 1:
            return sum(nums) == target
        key = (tuple(nums), k)
        if key in self.visited:
            return self.visited[key]
        size = len(nums)
        ans = False
        for x in range(1 << size):  # 2^size
            sums = 0
            rest = []
            for y in range(size):
                if (x >> y) & 1:
                    sums += nums[y]
                else:
                    rest.append(nums[y])
            if sums == target and self.solve(rest, target, k - 1):
                ans = True
                break
        self.visited[key] = ans
        return ans