G = [[] for i in range(21)]
City= {}
v = [0]*20
indeg = [0]*20
outdeg = [0]*20
nout = nin = nequ =0
success = False
def getCityIndex(p): 
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
def dfs(x):
    v[x] = 1
    if len(G[x]) > 0:
        for i in G[x]:
            if v[i.t] == 0:
                dfs(i.t)
class Edge:
    def __init__(self, s, t):
        self.s = s
        self.t = t
m = int(input())
for i in range(m):
    a, b = input().split()
    a = getCityIndex(a)
    b = getCityIndex(b)
    indeg[b] = indeg[b] + 1
    outdeg[a] = outdeg[a] + 1
    e1 = Edge(a, b)
    G[a].append(e1)
for i in range(len(City)):
    if indeg[i]!=outdeg[i]:
        if (indeg[i]-outdeg[i]) == 1:
            nin = nin + 1
        elif (outdeg[i]-indeg[i]) == 1:
            nout = nout + 1
            start = i
        else:
            break
    else:
        nequ = nequ + 1
if ((nin==1) and (nout==1) and (nequ==(len(City)-2))): 
    success = True
if ((nin==0) and (nout==0) and (nequ==len(City))):
    success = True
if (success):
    if (nout==1):
        dfs(start)
    if (nout==0):
        for i in range(len(City)) : 
            if outdeg[i]>0:
                dfs(i)
                break
for i in range(len(City)) :
    if v[i] == 0:
        success = False
        break
if (success):
    print("可以找到尤拉路徑")
else:
    print("無法找到尤拉路徑")
