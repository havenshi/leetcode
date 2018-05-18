nums=[[]]
sums = [0] * (len(nums) + 1)
for i in range(len(nums)):
    sums[i + 1] = sums[i] + nums[i]
print sums
print sums
