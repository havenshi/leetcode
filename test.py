def match(word1, word2):
    dp = [[True]*len(word2)]+[[False]*(len(word2)) for x in range(len(word1))]
    print dp
    for i in range(1,len(word1)+1):
        for j in range(len(word2)):
            if i == 2 and j == 1:
                print word1[i - 1], word2[j]
            if word1[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i-1][j-1]
            else:
                if i==2 and j == 1:
                    print word1[i-1],word2[j]
                dp[i][j] = (dp[i - 1][j-1] and word1[i-1] == word2[j])
    print dp
    return dp[-1][-1]
print match('b*d','bd')