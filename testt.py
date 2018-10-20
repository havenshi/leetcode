nums=[2,3]
i,j=0,1
for x in range((j-(i+1))/2+1):
    print x
    nums[i+1+x], nums[j-x] = nums[j-x], nums[i+1+x]
print nums