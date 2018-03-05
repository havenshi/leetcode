class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dictionary = {}
        for i in range(numCourses):
            dictionary[i] = 0
        for x in prerequisites:
            dictionary[x[0]] += 1

        ans = []
        queue = []
        for k, v in dictionary.items():
            if v == 0:
                queue.append(k)

        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop()
                ans.append(cur)
                for neighbor in [x[0] for x in prerequisites if x[1] == cur]:
                    dictionary[neighbor] -= 1
                    if dictionary[neighbor] == 0:
                        queue.append(neighbor)

        return ans if len(ans) == numCourses else []