class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # TLE
        self.result = []
        for i in range(1, len(num) + 1):  # parse first part with length of 1 and n
            if len(num[:i]) == 1 or (len(num[:i]) > 1 and num[:i][:1] != '0'):  # not start with '0'
                self.dfs(num[:i], num[i:], [num[:i]])

        self.answer = []  # [["1","0","0","1"],["10","0","1"],["100","1"],["1001"]]
        for res in self.result:
            self.helper(res[0], res[1:])
        return [x for x in self.answer if eval(x) == target]

    def dfs(self, before, after, tmp):
        if not after:
            self.result.append(tmp)
            return
        for i in range(1, len(after) + 1):
            if len(after[:i]) == 1 or (len(after[:i]) > 1 and after[:i][:1] != '0'):
                copytmp = tmp[:]
                self.dfs(before + after[:i], after[i:], copytmp + [after[:i]])

    def helper(self, before, after):
        if not after:
            self.answer.append(before)
            return
        self.helper(before + '+' + after[0], after[1:])
        self.helper(before + '-' + after[0], after[1:])
        self.helper(before + '*' + after[0], after[1:])
