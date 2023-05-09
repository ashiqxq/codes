def find(n):
    if n==parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(pa, pb):
    if R[pa]>=R[pb]:
        R[pa]+=R[pb]
        parent[pb]=pa
    else:
        R[pb]+=R[pa]
        parent[pa] = pb
        
        
check = []
parent = [i for i in range(26)]
R = [1 for i in range(26)]

for edge in equations:
    u, v = ord(edge[0])-97, ord(edge[-1])-97
    pu, pv = find(u), find(v)
    if pu!=pv:
        union(pu, pv)


def find(x):
    if ancestor[x] != x:
        ancestor[x] = find(ancestor[x])
    return ancestor[x]

def union(a, b):
    if rank[a]<rank[b]:
        ancestor[find(a)] = find(b)
        rank[b]+=1
    else:
        ancestor[find(b)] = find(a)
        rank[a]+=1

rank = [0 for i in s]
ancestor = list(range(len(s)))
for a, b in pairs:
    union(a, b)