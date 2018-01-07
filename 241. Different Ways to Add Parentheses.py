class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # method1, recursion, Divide and conquer
        if input.isdigit():
            return [int(input[0])]
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