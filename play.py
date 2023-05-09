# 1 - 3 - 6 - 10
# 2 - 5 - 9 - 14
# 4 - 8 - 13 - 


n = 10
grid1 = [[0 for i in range(n+1)] for j in range(n+1)]
dct = {}
mod = 1e9+7
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1:
            grid1[i][j] = grid1[i][j-1]+j
            continue
        if j==1:
            grid1[i][j] = grid1[i-1][j]+i-1
            continue
        grid1[i][j] = grid1[i-1][j]+grid1[i][j-1]-grid1[i-1][j-1]+1
sumgrid = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sumgrid[i][j] = sumgrid[i][j-1]+sumgrid[i-1][j]-sumgrid[i-1][j-1]+(grid1[i][j]*grid1[i][j])
        print(23, sumgrid[i][j])
        dct[grid1[i][j]] = sumgrid[i][j]%mod
        print(24, sumgrid[i][j], dct[grid1[i][j]], sumgrid[i][j]%mod)


ans = []
t = int(input())
for _ in range(t):
    x = int(input())
    # print(dct[x])
    ans.append(dct[x])
for val in ans:
    print(val)