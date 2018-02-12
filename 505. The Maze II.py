# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.
#
# Given the ball position, the hole position and the maze, your job is to find out how the ball could drop into the hole by moving shortest distance in the maze. The distance is defined by the number of empty spaces the ball go through from the start position (exclude) to the hole (include). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there may have several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and hole coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
#
# Output: "lul"
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# Output: "impossible"
# Explanation: The ball cannot reach the hole.
#
# Note:
#
# There are only one ball and one hole in the maze.
# The ball and hole will only exist in the empty space, and they will not at the same position initially.
# The given maze doesn't contain border (like the red rectangle in the example pictures), but you should assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and the length and width of the maze won't exceed 30.

# 首先预处理迷宫maze中各点坐标向四个方向运动最终可以达到的坐标，用数组dmap记录。
#
# 例如dmap[(3, 2)]['u']表示从坐标(3, 2)出发向上运动最终可以到达的位置。
#
# 利用数组bmap记录迷宫中各点坐标到小球初始位置的最短距离dist与最短路径path。
#
# 维护队列queue，初始将(ball, 0, '')加入queue（坐标，距离，路径）
#
# 记当前坐标为p，从p出发，分别向u, d, l, r四个方向扩展并更新下一个坐标np的最短距离与路径，保存在bmap中。
#
# 如果np得到更新，则将np加入队列；重复此过程直到queue为空
#
# 返回bmap[hole]