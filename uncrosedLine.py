def maxUncrossedLines(A,B):
    lA = len(A)
    lB = len(B)
    dp = [[ 0 for i in range(lB+1)] for j in range(lA+1)]
    for i in range(lA):
        for j in range(lB):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
    return dp[lA][lB]

print(maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
