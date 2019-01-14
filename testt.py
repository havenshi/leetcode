class Solution(object):
    def kDifference(self, a, k):
        """
        input nums: List[int]
        input ex: int
        output: List[List[int]]
        """
        dic = {}
        ans = 0
        for i in a:
            dic[i] = False                             # use dictionary to record abs(item-k)
        for i in dic:
            if dic[i] == False:
                if i-k in dic and dic[i-k] == False:  # if abs(current item-k) is in dictionary, index of current item and original index will be a pair
                    ans += 1                           # increasing result by 1
                if i+k in dic and dic[i+k] == False:
                    ans += 1
                dic[i] = True                          # mark as True
        return ans
if __name__ == "__main__":
    answer=Solution()
    print answer.kDifference([2,6,3,1,5,4,9,5,2], 3) # 4
    print answer.kDifference([1,5,3,4,2], 2)         # 3
    print answer.kDifference([5,5,2], 3)   # 1

