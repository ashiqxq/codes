from collections import deque


directions = [[1, 0],[-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def isValidBlock(i, j): 
    if (i>=0 and i<m and j>=0 and j<n):
        return True
    return False
def bfs(si, sj, rem):
    queue = deque()
    queue.append([si, sj, 0])
    dis[si][sj] = 0
    while queue:
        i, j, d = queue.popleft()
        for direction in directions:
            ni, nj = i+direction[0], j+direction[1]
            if isValidBlock(ni, nj):
                dis[ni][nj] = d+1
                queue.append([ni, nj, d+1])