class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candynum = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)): # from begin to end, if increase add 1
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        for i in range(len(ratings)-2, -1, -1): # from end to begin, if increase add 1
            if ratings[i] > ratings[i+1] and candynum[i+1] >= candynum[i]:
                candynum[i] = candynum[i+1] + 1
        return sum(candynum)

if __name__ == '__main__':
    answer = Solution()
    print answer.candy([1,2,3,5,4,3,2,3,4,2,4,4,6])