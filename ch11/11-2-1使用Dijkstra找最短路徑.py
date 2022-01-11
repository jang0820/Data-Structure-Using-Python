from heapq import *
City = {}
G = {} 
pq = []
dis = [1000000]*101
v = [0]*101
def getCityIndex(p): 
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w
        
n = int(input())
for i in range(n):
    a, b, w = input().split()
    a=getCityIndex(a)
    b=getCityIndex(b)
    w = int(w)
    e1 = Edge(a, b, w)
    e2 = Edge(b, a, w)
    if a in G.keys(): 
        G[a].append(e1)
    else:              
        G[a]=[e1]
    if b in G.keys():  
        G[b].append(e2)
    else:             
        G[b]=[e2]
        
s = getCityIndex(input())
p = (0, s)  #(距離,目標點)的tuple
heappush(pq, p)
dis[s]=0
while len(pq) > 0:        
    p = heappop(pq)
    s = p[1]
    if v[s] == 0:
        v[s] = 1
        for edge in G[s]:
            if v[edge.t] == 0:
                if dis[edge.t] > dis[s] + edge.w:
                    dis[edge.t] = dis[s] + edge.w
                    p = (dis[edge.t], edge.t)#(距離,目標點)的tuple
                    heappush(pq, p)
for i in range(len(City)):
    print(dis[i]," ", sep="", end="")
print()

