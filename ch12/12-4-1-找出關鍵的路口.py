G = [[] for i in range(100)]
City= {}
v = [0]*100
up = [0]*100
ar = [0]*100
t = 0
cnt = 0
def getCityIndex(p): 
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
def dfs(p, i):
    global t,cnt
    t = t + 1
    v[i] = t
    up[i] = t 
    child = 0 
    ap = False
    for e in G[i]:
        target = e.t
        if target != p:
            if v[target] > 0:
                up[i] = min(up[i],v[target])
            else:
                child = child + 1 
                dfs(i,target)
                up[i] = min(up[i], up[target]) 
                if up[target] >= v[i]: 
                    ap = True
    if (i == p and child > 1) or (i!=p and ap==True):
        ar[i] = 1
        cnt = cnt + 1
class Edge:
    def __init__(self, s, t):
        self.s = s
        self.t = t
n, m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    a, b = input().split()
    a = getCityIndex(a)
    b = getCityIndex(b)
    e1 = Edge(a, b)
    e2 = Edge(b, a)             
    G[a].append(e1)
    G[b].append(e2)
dfs(0, 0)
print(cnt)
for i in range(n):
    if ar[i] == 1:
        print(list(City.keys())[i])
