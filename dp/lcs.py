def lcs(text1, text2):
    l1, l2 = len(text1), len(text2)
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if text1[i-1]==text2[j-1]: dp[i][j] = 1+dp[i-1][j-1]
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[l1][l2]