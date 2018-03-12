# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
#
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
#
# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
#
# Example:
#
# Input:
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
#
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#
# Note:
#
# The range of width and height of the input 2D array is [1,500].

class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1
        ans = 0
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    if rows[x] == 1:
                        if cols[y] == 1:
                            ans += 1
        return ans