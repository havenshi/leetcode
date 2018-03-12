nums = [0,0,1,1,0,1,0,1,1,1,0,0,1]
res = 0
s, e = -1, -1
for i in range(len(nums)):

    if nums[i] == 1:
        if s==-1:
            s,e = i,i
        else:
            e+=1
        res = max(res, e - s + 1)

    else:
        s, e = -1, -1

print res