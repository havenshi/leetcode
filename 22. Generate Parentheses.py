# Time:  O(4^n / n^(3/2)) ~= Catalan numbers -> O(n!)
# Space: O(2^n)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, left, right, item, result):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(item)
        if left > 0:
            self.helper(left - 1, right, item + '(', result)
        if right > 0:
            self.helper(left, right - 1, item + ')', result)

        # mylist=[]
        # if n == 0:
        #     return []
        # else:
        #     if n == 1:
        #         return ["()"]
        #     else:
        #         for item in self.generateParenthesis(n-1):
        #             for i in range(0,(n-1)*2):
        #                 newp="("+item[:i]+")"+item[i:]
        #                 if newp not in mylist:
        #                     mylist.append(newp)
        #         return mylist

if __name__ == "__main__":
    answer=Solution()
    print answer.generateParenthesis(3)
