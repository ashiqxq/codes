from collections import deque
def solve(graph, degree):
    order = []
    queue = deque()
    for key, val in degree.items():
        if val==0:
            queue.append(key)
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            degree[v] -= 1
            if degree[v]==0:
                queue.append(v)

    return order
        
indegree = [0 for i in range(n)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    indegree[v] += 1
    solve(graph, indegree)
