class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contentDict = collections.defaultdict(list)
        for path in paths:
            parts = path.split()
            dir, files = parts[0], parts[1:]
            for file in files:
                tokens = file.split('.')
                name, content = tokens[0], tokens[1][4:-1]
                contentDict[content].append(dir + '/' + name + '.txt')
        return [g for g in contentDict.values() if len(g) > 1]
