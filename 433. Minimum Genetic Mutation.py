class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = list(set(bank))
        if end not in bank:
            return -1
        if start in bank:
            bank.remove(start)
        queue = [start]
        goal = {start: 0}
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur == end:
                    return goal[cur]
                for i in range(len(cur)):
                    c1 = cur[:i]
                    c2 = cur[i+1:]
                    for j in ['A', 'C', 'G', 'T']:
                        new = c1 + j + c2
                        if new in bank:
                            queue.append(new)
                            goal[new] = goal.get(cur, 0) + 1
                            bank.remove(new)
        return -1


if __name__ == "__main__":
    answer=Solution()
    print answer.minMutation("AAAACCCC",
"CCCCCCCC",
["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"])