
parent = [i for i in range(n+1)]

def find(a):
    while a!=parent[a]:
        a = parent[a]
    return a

def union(a, b):
    pa, pb = find(a), find(b)
    parent[pb] = pa
