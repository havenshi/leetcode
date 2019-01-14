class Solution(object):
    def missingWords(self, s, t):
        """
        input s: string
        input t: string
        output: string
        """
        res = []
        ss = s.split()
        tt = t.split()
        i, j = 0, 0
        while i < len(ss) and j < len(tt):  # use two pointers for both of strings, do iteration
            if ss[i] == tt[j]:
                i += 1
                j += 1
            else:
                res.append(ss[i])
                i += 1
        if i < len(ss):                       # if pointer of s does not arrive the end, append all items to result
            res.extend(ss[i:])
        return " ".join(res)

if __name__ == "__main__":
    answer=Solution()
    s = "I am using hackerrank to improve programming"
    t = "am hackerrank to improve"
    print answer.missingWords(s, t)