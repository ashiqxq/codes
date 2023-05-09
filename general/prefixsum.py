def prefixsum1D(arr):
    n = len(arr)
    ans = [0 for i in range(n)]
    ans[0] = arr[0]
    for i in range(1, n):
        ans[i] = ans[i-1]+arr[i]

def prefixsum2D(arr):
    #sum for i, j in original array is stored in i+1, j+1 in ans array
    m, n = len(arr), len(arr[0])
    ans = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            ans[i][j] = arr[i-1][j-1]+ans[i][j-1]+ans[i-1][j]-ans[i-1][j-1]
    return ans