# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
#
# For example, given the following image:
#
# [
#     "0010",
#     "0110",
#     "0100"
# ]
# and x = 0, y = 2,
#
# Return
# 6.

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # method1, O(m*n)
        left, right, up, down = y, y, x, x
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == '1':
                    left = min(left, j)
                    right = max(right, j)
                    up = min(up, i)
                    down = max(down, i)
        return (right - left + 1) * (down - up + 1)