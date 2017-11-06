class Solution():
    def toll_road(self, x, t, n):
        l = [None] * n
        for j in range(n-1, -1, -1):
            for i in range(j - 1, -1, -1):  # reversed traversal
                if x[j] - x[i] >= 10:
                    l[j] = i+1  # set the value of l[j] as the index i
                    break
        # l = [None, None, 1, 2]

        a = [0] * n
        for j in range(n):
            if j == 0 or l[j] == None:
                # initial a, if distance x1 is greater than 10, the revenue equals to value t1
                # if not, the initial revenue is 0
                a[j] = t[j] if x[j] >= 10 else 0

            else:
                # revenue is the maximum of:
                # a.the last revenue
                # b.and the last toll booths it can reach plus the value of jth itself
                a[j] = max(a[j - 1], a[l[j]-1] + t[j])
        # a = [50, 60, 100, 100]
        return a[-1]


if __name__ == '__main__':
    answer = Solution()
    print answer.toll_road([10,15,23,30],[50,60,50,10],4)
