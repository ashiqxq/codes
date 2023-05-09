def diagonalHopTrav(mat):
    m, n, vals = len(mat), len(mat[0]), []
    for i in range(m):
        for j in range(n):
            vals.append(mat[i][j])
            mat[i][j] = -1
    vals.sort()
    i, j, vi, start_i, start_j, lastisflip = 0, 0, 0, 0, 0, False
    print("vals", vals)
    while True:
        if i<0:     i = 0
        if j<0:     j = 0
        if i>=m:    i, j = min(i, m-1), j+1
            
        if mat[i][j] == -1:
            mat[i][j], vi = vals[vi], vi+1
            if i == m-1 and j == n-1:   break
                
        else:
            i, j, start_i, start_j, lastisflip = getnew(i, j, start_i, start_j, m, n)
            continue
            
        if i==j or (abs(i-j)==1 and (mat[i][j]==1 and mat[j][i]==1)):
            i, j, start_i, start_j, lastisflip = getnew(i, j, start_i, start_j, m, n)
            continue
            
        else:
            if not lastisflip:  i, j, lastisflip = j, i, True
            else:
                if i<j: j-=1; i+=1
                else:   i-=1; j+=1
    return mat 
