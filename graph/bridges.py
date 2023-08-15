#backedges can never be bridges
#in a dfs tree traversal, the edge i.e not traversed and it connects decendant to an 
#ancestor that is not a parent. this is a backedge
def find_bridges():
    timer = 0
    visited = [0 for i in range(n)]
    tin = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    def dfs(v, p = -1):
        visited[v] = 1
        tin[v], low[v] = timer, timer
        timer += 1
        for to in adj[v]:
            if to == p: continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if (low[to] > tin[v]):
                    # edge [v, to] is a bridge

    for i in range(n):
        if not visited[i]:
            dfs(i, -1)