# time:O(n)
# space:O(n)
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        import collections
        hashmap = collections.defaultdict(list)
        for each_d in d:
            hashmap[each_d[0]].append((0, each_d))
        # {'a': [(0, 'ale'), (0, 'apple')], 'p': [(0, 'plea')], 'm': [(0, 'monkey')]}

        ans = []
        for each_s in s:
            pairs = hashmap[each_s]  # find all pairs begins with current string
            del hashmap[each_s]
            for (i, p) in pairs:
                if i == len(p) - 1:  # if current position is the last string of the d word
                    ans.append(p)
                else:
                    hashmap[p[i + 1]].append((i + 1, p))

        if not ans:
            return ''

        max_length = max([len(a) for a in ans])
        return min([a for a in ans if len(a) == max_length])