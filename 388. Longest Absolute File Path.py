class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0

        input = '\n'.join(input.split('\n '))
        input = '\t'.join(input.split('\t '))
        self.res = 0
        flag = '\n\t'
        if flag not in input and '.' in input:
            return max(self.res, len(input))
        input = input.replace(flag + '\t', (len(flag) + 2) * '#')
        inputlist = input.split(flag)
        inputlist = [i.replace((len(flag) + 2) * '#', flag + '\t') for i in inputlist]

        for i in range(1, len(inputlist)):
            self.dfs(len(inputlist[0]), inputlist[i], layer=1)
        return self.res

    def dfs(self, length, input, layer):
        if not input:
            self.res = max(self.res, length)
            return
        flag = '\n\t' + '\t' * layer
        if flag not in input:
            if len(input) >= 1 and '.' in input:
                self.res = max(self.res, length + len(input) + 1)
            return
        input = input.replace(flag + '\t', (len(flag) + 2) * '#')
        inputlist = input.split(flag)
        inputlist = [i.replace((len(flag) + 2) * '#', flag + '\t') for i in inputlist]
        for i in range(1, len(inputlist)):
            self.dfs(length + len(inputlist[0]) + 1, inputlist[i], layer + 1)