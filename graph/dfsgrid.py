
directions =[[1, 0],[-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]] if (diagonalAllowed) else  [[1, 0],[-1, 0], [0, 1], [0, -1]]  

def isValidBlock(i, j, m, n): 
    if (i>=0 and i<m and j>=0 and j<n):
        return True
    return False

def dfs(i, j):
    grid[i][j].visited = True
    for k in range(len(directions)):
        [ni, nj] = [i+directions[k][0], j+directions[k][1]]
        if (isValidBlock(ni, nj)):
            dfs(ni, nj)
  