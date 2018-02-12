# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: false
# Explanation: There is no way for the ball to stop at the destination.
#
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
#
# 这道题让我们遍历迷宫，但是与以往不同的是，这次迷宫是有一个滚动的小球，这样就不是每次只走一步了，而是朝某一个方向一直滚，
# 直到遇到墙或者边缘才停下来，我记得貌似之前在手机上玩过类似的游戏。那么其实还是要用DFS或者BFS来解，只不过需要做一些修改。
# 先来看DFS的解法，我们用DFS的同时最好能用上优化，即记录中间的结果，这样可以避免重复运算，提高效率。
# 我们用二维数组dp来保存中间结果，然后用maze数组本身通过将0改为-1来记录某个点是否被访问过，这道题的难点是在于处理一直滚的情况，
# 其实也不难，只要我们有了方向，只要一直在那个方向上往前走，每次判读是否越界了或者是否遇到墙了即可，然后对于新位置继续调用递归函数