# -*- coding: utf-8 -*-
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # 最左下/最左上/最右下/最右上的四个点只出现过一次,其他肯定是出现两次和四次(保证完全覆盖)
        # 上面四个点围成的面积,正好等于所有子矩形的面积之和(保证不重复)
        corners = {}
        area = 0
        # 找到四个点
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        for sub in rectangles:
            ax, ay, bx, by = sub[:]
            area += (bx - ax) * (by - ay)  # 计算面积并加到总面积

            points = [(ax, ay), (bx, by), (ax, by), (bx, ay)]  # 对所有点计数
            for point in points:
                if point in corners:
                    corners[point] += 1
                else:
                    corners[point] = 1

        if area != (top - bottom) * (right - left):
            return False

        big_four = [(left, bottom), (right, top), (left, top), (right, bottom)]

        for bf in big_four:  # 如果四个点出现多于一次，false
            if bf not in corners or corners[bf] != 1:
                return False

        for key in corners:  # 如果里面的点出现不为两次货四次，false
            if corners[key] % 2 and key not in big_four:
                return False

        return True