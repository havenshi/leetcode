class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # [0,6,1,2,4,5,3,7]
        d = {}
        for i, v in enumerate(row):
            d[v] = i  # 记录每个值的位置
        # {0: 0, 1: 2, 2: 3, 3: 6, 4: 4, 5: 5, 6: 1, 7: 7}
        ret = 0
        for i in range(0, len(row), 2):
            cp = row[i] ^ 1
            if row[i + 1] == cp: continue  # 遇到一个不是cp的，就把cp交换到旁边
            d[row[i + 1]] = d[cp]  # 注意构建dictionary很关键，类似于unionfind island那题。把这个异值6的位置更新至2，即cp的位置上。不用更新cp的位置因为接下来cp就要被换到正确的位置了。
            # {0: 0, 1: 2, 2: 3, 3: 6, 4: 4, 5: 5, 6: 2, 7: 7}

            row[i + 1], row[d[cp]] = cp, row[i + 1]  # 交换i+1（异值）和cp，但此时cp位置的value可能已经变动了，所以从dictionary里找
            # [0, 1, 6, 2, 4, 5, 3, 7]
            ret += 1

        return ret

