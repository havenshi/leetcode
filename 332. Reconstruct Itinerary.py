# Time:  O(t! / (n1! * n2! * ... nk!)), t is the total number of tickets,
#                                       ni is the number of the ticket which from is city i,
#                                       k is the total number of cities.
# Space: O(t)
import collections

# dfs，只是有点慢。。。

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.routes = collections.defaultdict(list)
        for s, e in tickets:
            self.routes[s].append(e)
        for value in self.routes.values():
            value.sort()

        self.res = []
        self.dfs("JFK", tickets, ["JFK"])
        return self.res

    def dfs(self, start, tickets, tmp):
        if self.res:  # 这个添加比较重要，否则self.res就一直append各种符合条件的解，而实际上只要返回排序后的第一个解就可以了
            return

        if len(tmp) == len(tickets) + 1:
            self.res = tmp
            return
        elif start not in self.routes:
            return
        for end in self.routes[start]:
            ind = self.routes[start].index(end)  # 因为ticket只能买一次，所以要重复remove和insert的操作
            self.routes[start].remove(end)

            copytmp = tmp[:]
            copytmp.append(end)
            self.dfs(end, tickets, copytmp)

            self.routes[start].insert(ind, end)


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.routes = collections.defaultdict(list)
        for s, e in tickets:
            self.routes[s].append(e)
        return self.solve("JFK")

    def solve(self, start):
        left, right = [], []
        for end in sorted(self.routes[start]):
            if end not in self.routes[start]:
                continue
            self.routes[start].remove(end)
            subroutes = self.solve(end)
            if start in subroutes:
                left += subroutes
            else:
                right += subroutes
        return [start] + left + right