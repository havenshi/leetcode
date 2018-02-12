# -*- coding:utf8 -*-
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.trie = Trie()
        for word in words:
            self.trie.insert(word) # 将待查找的单词储存在字典树Trie中


        self.result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board[i][j], board, i, j, self.trie.root)
        return sorted(self.result)

    def dfs(self, word, board, i, j, node):# dfs时，如果当前形成的单词不在Trie里，就没必要继续dfs下去了。如果当前字符串在trie里，就说明board可以形成这个word。
        node = node.children.get(board[i][j])
        if node is None: # 使用DFS（深度优先搜索）在格板中查找，利用字典树剪枝
            return
        if node.isWord: # 每当找到一个单词时，将该单词加入答案中，并从字典树中删去
            self.result.append(word)
            self.trie.delete(word)
            # 注意此时不能return
        tmp = board[i][j]
        board[i][j] = "#"
        map = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for m in map:
            if i + m[0] >= 0 and i + m[0] < len(board) and j + m[1] >= 0 and j + m[1] < len(board[0]):
                self.dfs(word + board[i + m[0]][j + m[1]], board, i + m[0], j + m[1], node)
        board[i][j] = tmp


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False  # if this node store a word

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if child is None:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    def delete(self, word):
        """
        Delete if the node has no child.
        :type word: str
        :rtype: void
        """
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node)) # 记录位置和node
            child = node.children.get(letter)
            if child is None:
                return False# 未找到word
            node = child
        if not node.isWord:
            return False
        if len(node.children):
            node.isWord = False
        else: # 每当找到一个单词时，将该单词从字典树中删去。
            for (letter, node) in reversed(queue):
                del node.children[letter]
                if len(node.children) or node.isWord: # 如果有其他子节点，则不能继续往上删
                    break
        return True

if __name__ == "__main__":
    answer=Solution()
    print answer.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
["oath","pea","eat","rain"])