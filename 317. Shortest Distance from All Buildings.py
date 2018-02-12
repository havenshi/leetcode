# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
#
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

# 我们可以从一个建筑物出发来计算每一个空地到这个建筑物的距离, 然后设置一个数组sumDistance来累加统计从一个空地出发到
# 其他所有建筑物的距离.即sumDistance[i][j]代表从位置grid[i][j]出发到其他建筑物的距离之和.