G = [[] for i in range(51)]
indeg = [0]*51
v = [0]*51
cnt = 0
class Edge:
    def __init__(self, s, t):
        self.s = s
        self.t = t
n,m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    indeg[b] = indeg[b] + 1
    e1 = Edge(a, b)
    G[a].append(e1)
i = 0
while i < n:
    if indeg[i] == 0 and v[i] == 0:
        v[i] = 1
        cnt = cnt + 1
        print(i," ", sep = "",end = "")
        for item in G[i]:
            indeg[item.t] = indeg[item.t] - 1
    if (cnt == n):
        break
    if i == n-1:
        i = -1
    i = i + 1
    
