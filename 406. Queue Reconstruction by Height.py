class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        def sorter(x, y):
            if x[0] != y[0]:
                return y[0] - x[0]
            else:
                return x[1] - y[1]

        new_people = sorted(people, cmp=sorter)

        res = []
        for p in new_people:
            res.insert(p[1], p)
        return res