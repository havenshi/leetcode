class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import collections
        dict_sec = collections.Counter(secret)
        dict_gue = collections.Counter(guess)

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        cows = 0
        for k in dict_gue.keys():
            number = dict_sec.get(k, 0)
            cows += min(number, dict_gue[k])
        return str(bulls) + 'A' + str(cows - bulls) + 'B'