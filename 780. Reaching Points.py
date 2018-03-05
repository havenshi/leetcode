class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        # if (sx+sy,sy) or (sx,sy+sx) reach (tx,ty)
        while tx > sx and ty > sy:
            if tx > ty: # 类似于辗转相除法（欧几里得算法）
                tx %= ty
            else:
                ty %= tx
        if sx == tx and (ty-sy)%sx == 0:
            return True
        if sy == ty and (tx-sx)%sy == 0:
            return True
        return False