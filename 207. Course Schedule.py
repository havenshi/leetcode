class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        in_degree = {}
        graph = {}
        for u in range(numCourses):
            in_degree[u] = 0
            graph[u] = []
        for item in prerequisites:
            in_degree[item[1]] += 1
            graph[item[0]].append(item[1])

        print in_degree
        print graph

        Q = []
        for u in in_degree:
            if in_degree[u] == 0:
                Q.insert(0, u)

        print Q

        while Q:
            u = Q.pop()
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] < 0:  # if not enough degree
                    return False
                elif in_degree[v] == 0:
                    Q.insert(0, v)

        if (not 0) in in_degree.values():  # if degree is not all used
            return False
        else:
            return True

if __name__ == "__main__":
    answer = Solution()
    print answer.canFinish(2, [[1,0]])