# 由于题目中要求我们用置换方法in-place来解题，所以我们就不能新建一个相同大小的数组，那么我们只能更新原有数组，
# 但是题目中要求所有的位置必须被同时更新，但是在循环程序中我们还是一个位置一个位置更新的，那么当一个位置更新了，
# 这个位置成为其他位置的neighbor时，我们怎么知道其未更新的状态呢，我们可以使用状态机转换：
#
# 状态0： 死细胞转为死细胞
#
# 状态1： 活细胞转为活细胞
#
# 状态2： 活细胞转为死细胞
#
# 状态3： 死细胞转为活细胞
#
# 最后我们对所有状态对2取余，那么状态0和2就变成死细胞，状态1和3就是活细胞，达成目的。我们先对原数组进行逐个扫描，
# 对于每一个位置，扫描其周围八个位置，如果遇到状态1或2，就计数器累加1，扫完8个邻居，
# 如果少于两个活细胞或者大于三个活细胞，而且当前位置是活细胞的话，标记状态2，如果正好有三个活细胞且当前是死细胞的话，
# 标记状态3。完成一遍扫描后再对数据扫描一遍，对2取余变成我们想要的结果

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m else 0
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                ## Count live cells in 3x3 block.
                for I in xrange(max(i - 1, 0), min(i + 2, m)):
                    for J in xrange(max(j - 1, 0), min(j + 2, n)):
                        if (I != i or J != j) and (board[I][J] == 1 or board[I][J] == 2):
                            count += 1

                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 2
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 3

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] %= 2  # Update to the next state.