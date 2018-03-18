# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if beginWord not in wordList:
            wordList.append(beginWord)

        length = len(beginWord)
        self.preMap = {}
        for word in wordList:
            self.preMap[word] = []
        self.result = []
        cur_level = set()
        cur_level.add(beginWord)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                wordList.remove(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in wordList:
                                self.preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:  # not find endword
                return []
            if endWord in cur_level:
                break
        # preMap = {'cog': ['log', 'dog'], 'hit': [], 'log': ['lot'], 'dog': ['dot'], 'hot': ['hit'], 'lot': ['hot'], 'dot': ['hot']}, next:current

        self.buildPath([], endWord, self.preMap, self.result)
        return self.result

    def buildPath(self, path, word, preMap, result):
        if len(preMap[word]) == 0:  # if premap[endword] == [], it has no before word
            result.append([word] + path)  # add before word ahead of current word
            return
        path.insert(0, word)  # add current word ahead
        for w in preMap[word]:  # dfs, find the word before the current word
            self.buildPath(path, w, preMap, result)
        path.pop(0)  # recover

if __name__ == "__main__":
    answer=Solution()
    print answer.findLadders("hot", "dog", ["hot","dog","dot"])