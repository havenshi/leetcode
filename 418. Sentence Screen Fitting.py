# -*- coding: utf-8 -*-
# Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.
#
# Note:
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Example 1:
#
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
#
# Output:
# 1
#
# Explanation:
# hello---
# world---
#
# The character '-' signifies an empty space on the screen.
# Example 2:
#
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
#
# Output:
# 2
#
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
#
# The character '-' signifies an empty space on the screen.
# Example 3:
#
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
#
# Output:
# 1
#
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# The character '-' signifies an empty space on the screen.
#
# I-had
# apple
# pie-I
# had--
# apple
# pie-I
# had--
# apple
#上例中apple单词的相对位置从第二行开始循环，因此只需要找到单词相对位置的“循环节”

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        wcount = len(sentence)
        wlens = map(len, sentence)
        slen = sum(wlens) + wcount
        dp = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc, pw) in dp:
                pr0, ans0 = dp[(pc, pw)]
                loop = (rows - pr0) / (pr - pr0 + 1)
                ans = ans0 + loop * (ans - ans0)
                pr = pr0 + loop * (pr - pr0)
            else:
                dp[(pc, pw)] = pr, ans
            scount = (cols - pc) / slen
            ans += scount
            pc += scount * slen + wlens[pw]
            if pc <= cols:
                pw += 1
                pc += 1
                if pw == wcount:
                    pw = 0
                    ans += 1
            if pc >= cols:
                pc = 0
                pr += 1
        return ans

        # dictionary = {}
        # i= 0
        # for row in range(rows):
        #     words = []
        #     while len('-'.join(words+sentence[i+1])) <= cols:
        #         words.append(words+sentence[i+1])
        #         i += 1
        #     new_words = '-'.join(words) + (cols-len('-'.join(words)))*'-'
        #     if new_words not in dictionary:
        #         dictionary[row] = new_words
        #     else:
        #         break
        # return new_words
