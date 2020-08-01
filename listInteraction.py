def countSquares(matrix):
    n = len(matrix)
    m = len(matrix[0])
    ams = [[0]*(m+1) for _ in range(n+1)]
    # print(ams)
    c = 0
    for i in range(1,n+1):
        for j in range(1, m+1):
            if(matrix[i-1][j-1] == 1):
                ams[i][j] = 1 + min(ams[i][j-1], ams[i-1][j], ams[i-1][j-1])
                c += ams[i][j]
    return c

print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
