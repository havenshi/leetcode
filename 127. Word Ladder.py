import Queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
#         TLE
#         n = len(wordList)
#         if n == 0:
#             return []
#         q = [(beginWord, 1)]
#         while q:
#             current = q.pop(0)
#             currentWord = current[0]
#             currentStep = current[1]
#             if currentWord == endWord:
#                 return currentStep
#             for i in range(len(currentWord)):
#                 for j in [chr(x) for x in range(ord('a'), ord('z')+1)]:
#                     if j != currentWord[i]:
#                         newWord = currentWord[:i] + j + currentWord[i+1:]
#                         if newWord in wordList:
#                             q.append((newWord, currentStep+1))
#                             wordList.remove(newWord)
#         return 0

        # BFS
        wordSet = set([])
        for item in wordList:
            wordSet.add(item)   # transfer list into set
        queue = Queue.Queue()
        queue.put(beginWord)
        goal = {beginWord:1}
        char = [chr(i) for i in range(ord('a'), ord('z') + 1)]  # character list a~z
        while not queue.empty():  # BFS
            cur = queue.get()  # FIFO
            if cur == endWord:
                return goal[cur] # base
            while cur in wordSet:
                wordSet.remove(cur)  # remove duplicate
            for i in range(len(cur)):  # tranverse each position of current word
                p1 = cur[:i]
                p2 = cur[i + 1:]
                for j in char:
                    word = p1 + j + p2
                    if word in wordSet:
                        queue.put(word)
                        goal[word] = goal[cur] + 1  # new item, step + 1
                        wordSet.remove(word)  # important! if visited, should not visit again, so delete.
        return 0

if __name__ == "__main__":
    answer=Solution()
    print answer.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])