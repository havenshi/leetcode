# -*- coding: utf-8 -*-
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # 利用栈（Stack）数据结构。保存一个递增的栈。
        #
        # 首先将字符串以'\n'进行分割，得到目录 / 文件的列表，记为parts
        #
        # 然后统计各目录 / 文件中'\t'的个数，表示当前目录 / 文件的深度
        #
        # 遍历parts，若栈顶元素的深度不小于parts的深度，则弹出栈顶元素，重复此过程。
        #
        # 然后将新的深度压入栈中，顺便统计当前目录的总长度。
        ans = lengthSum = 0
        stack = [(-1, 0)]
        for p in input.split('\n'): # ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']
            depth = p.count('\t') # 计算深度
            name = p.replace('\t', '')
            topDepth, topLength = stack[-1] # stack中的深度及字符长度pair
            while depth <= topDepth:
                stack.pop()
                lengthSum -= topLength
                topDepth, topLength = stack[-1]
            length = len(name) + (depth > 0) # 例如深度为1，则结果字符串中加"/"
            lengthSum += length
            stack.append((depth, length))
            if name.count('.'):
                ans = max(ans, lengthSum)
        return ans

if __name__ == "__main__":
    print Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

    #     if not input:
    #         return 0
    #
    #     input = '\n'.join(input.split('\n '))
    #     input = '\t'.join(input.split('\t '))
    #     self.res = 0
    #     flag = '\n\t'
    #     if flag not in input and '.' in input:
    #         return max(self.res, len(input))
    #     input = input.replace(flag + '\t', (len(flag) + 2) * '#')
    #     inputlist = input.split(flag)
    #     inputlist = [i.replace((len(flag) + 2) * '#', flag + '\t') for i in inputlist]
    #
    #     for i in range(1, len(inputlist)):
    #         self.dfs(len(inputlist[0]), inputlist[i], layer=1)
    #     return self.res
    #
    # def dfs(self, length, input, layer):
    #     if not input:
    #         self.res = max(self.res, length)
    #         return
    #     flag = '\n\t' + '\t' * layer
    #     if flag not in input:
    #         if len(input) >= 1 and '.' in input:
    #             self.res = max(self.res, length + len(input) + 1)
    #         return
    #     input = input.replace(flag + '\t', (len(flag) + 2) * '#')
    #     inputlist = input.split(flag)
    #     inputlist = [i.replace((len(flag) + 2) * '#', flag + '\t') for i in inputlist]
    #     for i in range(1, len(inputlist)):
    #         self.dfs(length + len(inputlist[0]) + 1, inputlist[i], layer + 1)