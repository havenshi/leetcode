# 4，2，3
#
# -1，4，2，3
#
# 2，3，3，2，4
#
# 当我们发现后面的数字小于前面的数字产生冲突后，有时候需要修改前面较大的数字(比如前两个例子需要修改4)，
# 有时候却要修改后面较小的那个数字(比如前第三个例子需要修改2)，那么有什么内在规律吗？
# 是有的，判断修改那个数字其实跟再前面一个数的大小有关系，
# 首先如果再前面的数不存在，比如例子1，4前面没有数字了，我们直接修改前面的数字为当前的数字2即可。
# 而当再前面的数字存在，并且小于当前数时，比如例子2，-1小于2，我们还是需要修改前面的数字4为当前数字2；
# 如果再前面的数大于当前数，比如例子3，3大于2，我们需要修改当前数2为前面的数3。
# 这是修改的情况，由于我们只有一次修改的机会，所以用一个变量cnt，初始化为1，修改数字后cnt自减1，
# 当下次再需要修改时，如果cnt已经为0了，直接返回false。

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        chance = 1
        for x in range(len(nums)):
            if x and nums[x] < nums[x - 1]:
                if not chance:
                    return False
                chance -= 1
                if x > 1 and nums[x] <= nums[x - 2]:
                    nums[x] = nums[x - 1]
        return True