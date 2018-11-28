class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        len_M = len(M)
        group = [i for i in range(len_M)]
        count = len_M

        for i in range(len_M):
            for j in range(i + 1, len_M):
                if M[i][j] == 1:
                    p1 = self.find(i, group)
                    p2 = self.find(j, group)
                    if p1 != p2:
                        group[p2] = p1
                        count -= 1

                print group
        return count

    def find(self, x, lst):
        while x != lst[x]:
            x = lst[x]
        return x
if __name__ == "__main__":
    answer=Solution()
    print answer.findCircleNum([[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]
 )