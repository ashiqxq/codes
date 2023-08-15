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


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b) #this line is important for some cases
        if self.rank[a]<self.rank[b]:
            self.parent[self.find(a)] = self.find(b)
            self.rank[b]+=1
        else:
            self.parent[self.find(b)] = self.find(a)
            self.rank[a]+=1