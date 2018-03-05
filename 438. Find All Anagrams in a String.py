class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # method1
        import collections

        length = len(p)
        res = []
        if len(s) < length:
            return res

        dictionary = collections.Counter(s[:length])
        sample_dict = collections.Counter(p)
        if dictionary == sample_dict:
            res.append(0)

        for i in range(1, len(s) - length + 1):
            dictionary[s[i - 1]] -= 1
            if dictionary[s[i - 1]] == 0:
                del dictionary[s[i - 1]]
            dictionary[s[i + length - 1]] = dictionary.get(s[i + length - 1], 0) + 1
            if dictionary == sample_dict:
                res.append(i)

        return res

        # method2, hash为所有26个字母的计数，免去了反复del反复增加新key-value的情况，所以比method1快很多

        # if len(s) < len(p):
        #     return []
        # samplewindow = [0] * 26  # create sample window
        # for item in p:
        #     samplewindow[ord(item) - ord('a')] += 1
        #
        # result = []
        # window = [0] * 26
        # for i in range(len(p)):
        #     window[ord(s[i]) - ord('a')] += 1  # create first window
        # i = 0
        # while i <= len(s) - len(p):
        #     if window == samplewindow:
        #         result.append(i)
        #     # slice window
        #     window[ord(s[i]) - ord('a')] -= 1  # first position remove 1
        #     i += 1
        #     if i + len(p) - 1 < len(s):  # last position add 1
        #         window[ord(s[i + len(p) - 1]) - ord('a')] += 1
        # return result

if __name__ == '__main__':
    answer = Solution()
    print answer.findAnagrams( "cbaebabacd", "abc")