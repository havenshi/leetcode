class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # 我的dp解法，beat 97.53%
        # Time:  O(n^2)
        # Space: O(n^2)
        if input.isdigit():
            return [int(input)]
        n = len(input)
        self.dp = [[None] * n for x in range(n)]
        return self.helper(input, 0, n - 1)

    def helper(self, input, l, r):
        if input[l:r + 1].isdigit():
            self.dp[l][r] = [int(input[l:r + 1])]
            return self.dp[l][r]
        tmp = []
        for k in range(l + 1, r):
            if input[k] in ['-', '+', '*']:
                if self.dp[l][k - 1] is not None:
                    left = self.dp[l][k - 1]
                else:
                    left = self.helper(input, l, k - 1)

                if self.dp[k + 1][r] is not None:
                    right = self.dp[k + 1][r]
                else:
                    right = self.helper(input, k + 1, r)

                for eachleft in left:
                    for eachright in right:
                        if input[k] == '-':
                            tmp.append(eachleft - eachright)
                        elif input[k] == '+':
                            tmp.append(eachleft + eachright)
                        else:
                            tmp.append(eachleft * eachright)

        self.dp[l][r] = tmp
        return tmp




        # method1, recursion, Divide and conquer
        # Time:  O(3^n)
        # 因为T(n)=T(1)+T(n-1)+T(2)+T(n-2)+...+T(-11)+T(n)=2*(T(1)+...+T(n-1))，而T(n+1)=2*(T(1)+...+T(n))=T(n)+2T(n)=3T(n)
        # Space: O(n)
        if input.isdigit():
            return [int(input)]
        result = []
        for k, v in enumerate(input):
            if v in ['-', '+', '*']:
                left = self.diffWaysToCompute(input[:k])
                right = self.diffWaysToCompute(input[k + 1:])
                for l in left:
                    for r in right:
                        if v == '-':
                            result.append(int(l) - int(r))
                        elif v == '+':
                            result.append(int(l) + int(r))
                        else:
                            result.append(int(l) * int(r))
        return result


        # Time:  O(n*n!) 太慢，以至于没有出现在leetcode submiss图表中
        # Space: O(n)
        # method 2, add parentheses, Backtracking, O(n!)
        import re
        nums, ops = [], []
        input = re.split(r'(\D)', input)  # split by non-digit, ['2', '*', '3', '-', '4', '*', '5']
        for x in input:  # divide into digit and non-digit groups
            if x.isdigit():
                nums.append(x)
            else:
                ops.append(x)
        if not ops:
            return [int(nums[0])]
        self.result = []
        for i in range(len(ops)):
            self.helper(nums, ops, i)

        # ['(((2*3)-4)*5)', '((2*3)-(4*5))', '((2*(3-4))*5)', '(2*((3-4)*5))', '(2*(3-(4*5)))']
        return [eval(x) for x in self.result]

    def helper(self, nums, ops, i):
        tmp = nums[i] + ops[i] + nums[i + 1]  # calculate 3+4 and insert into nums
        newnums = nums[:i] + nums[i + 2:]  # delete ith and (i+1)th from nums
        newops = ops[:i] + ops[i + 1:]  # delete ith from ops
        newnums.insert(i, '(' + str(tmp) + ')')  # expression, so add '()'
        if not newops:
            if newnums[0] not in self.result:  # if expression is not duplicate(e.g, two (2*3)-(4*5))
                self.result.append(newnums[0])
            return
        for i in range(len(newops)):
            self.helper(newnums, newops, i)


if __name__ == '__main__':
    answer = Solution()
    print answer.diffWaysToCompute("2*3-4*5")