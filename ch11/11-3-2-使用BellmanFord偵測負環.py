City = {}
G = {} 
def getCityIndex(p): 
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w      
m = int(input())
for i in range(m):
    a, b, w = input().split()
    a=getCityIndex(a)
    b=getCityIndex(b)
    w = int(w)
    e1 = Edge(a, b, w)
    if a in G.keys(): 
        G[a].append(e1)
    else:              
        G[a]=[e1]     
def BellmanFord(s):
    qu = []
    dis = [1000000]*101
    inqu = [0]*101
    cnt = [0]*101
    qu.append(s)
    dis[s] = 0
    inqu[s] = 1
    while len(qu) > 0:
        p = qu.pop(0)
        inqu[p] = 0
        if G.get(p) != None:
            for edge in G[p]:
                if dis[edge.t] > dis[edge.s] + edge.w:
                    dis[edge.t] = dis[edge.s] + edge.w
                    cnt[edge.t] = cnt[edge.t] + 1
                    if cnt[edge.t] > len(City):
                        return True
                    if inqu[edge.t] == 0:
                        qu.append(edge.t);
                        inqu[edge.t]=1;
    return False
ans = False
for i in range(len(City)):
    ans = BellmanFord(i)
    if ans:
        break
if ans:
    print("找到負環")
else:
    print("找不到負環")
