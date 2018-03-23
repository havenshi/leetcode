class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # TLE，"3456237490", 9191超时，但'123456789',45不超时
        if not num:
            return []
        self.answer = []
        self.visits = {}
        for item in self.dfs(num):
            if eval(item) == target:
                self.answer.append(item)
        return self.answer

    def dfs(self, num):
        if num in self.visits:
            return self.visits[num]

        if len(num) == 1:
            self.visits[num] = num
            return set([num])

        dictionary = set([])
        for i in range(1, len(num)):
            for before in self.dfs(num[:i]):
                for after in self.dfs(num[i:]):
                    plus = before + '+' + after
                    dictionary.add(plus)

                    minus = before + '-' + after
                    dictionary.add(minus)

                    times = before + '*' + after
                    dictionary.add(times)

        if num[:1] != '0':  # not start with '0'
            dictionary.add(num)

        self.visits[num] = dictionary  # memorization

        return dictionary



        # TLE
        self.answer = []
        self.visits = {}
        for k in self.dfs(num):
            if k == target:
                self.answer += self.dfs(num)[k]
        return self.answer

    def dfs(self, num):
        if num in self.visits:
            return self.visits[num]

        if len(num) == 1:
            self.visits[num] = {int(num[0]): num[0]}
            return {int(num[0]): num[0]}
        dictionary = collections.defaultdict(set)
        for i in range(1, len(num)):  # parse first part with length of 1 and n-1
            # 如果能仅拆成两段就好了。但是dictionary使用value记录，就是说'2+3*2'只能拆成'2+3’和‘2'，但'2+3*2’==8，无法找出该解
            for before_k in self.dfs(num[:i]):
                before_v = self.dfs(num[:i])[before_k]
                for after_k in self.dfs(num[i:]):
                    after_v = self.dfs(num[i:])[after_k]

                    plus = set([b + '+' + a for b in before_v for a in after_v])
                    dictionary[eval(str(before_k) + '+' + str(after_k))] |= plus

                    minus = set([])
                    for b in before_v:
                        for a in after_v:
                            aa = [x for x in a if not x.isdigit()]
                            if not aa or (not '-' in aa and not '+' in aa):
                                minus.add(b + '-' + a)
                            dictionary[eval(str(before_k) + '-' + str(after_k))] |= minus  # -减号要求表达式中不能含‘-’

                    times = set([])
                    for b in before_v:
                        bb = [x for x in b if not x.isdigit()]
                        for a in after_v:
                            aa = [x for x in a if not x.isdigit()]
                            if (not bb or (not '-' in bb and not '+' in bb)) and (
                                not aa or (not '-' in aa and not '+' in aa)):
                                times.add(b + '*' + a)  # 因为不能用括号，所以*乘号要求表达式中不能含‘+-’
                            dictionary[eval(str(before_k) + '*' + str(after_k))] |= times
        if len(num) == 1 or (len(num) > 1 and num[:1] != '0'):  # not start with '0'
            dictionary[int(num)] |= set([num])
        self.visits[num] = dictionary

        return dictionary



        # TLE
        # Time:  O(n*n!)
        # Space: O(n)
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

if __name__  == '__main__':
    print Solution().addOperators("123",6)