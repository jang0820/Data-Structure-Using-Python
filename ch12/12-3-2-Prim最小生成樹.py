import heapq
pq = []
G = [[] for i in range(100)]
ans = []
v = [0]*101
dist = [100000000]*101
class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w
n,m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    e1 = Edge(a, b, w)
    e2 = Edge(b, a, w)
    G[a].append(e1)
    G[b].append(e2)
start = 0
v[start] = 1
dist[start] = 0
numEdge = result = 0
for e in G[start]:
    if e.w < dist[e.t]:
        dist[e.t] = e.w
        heapq.heappush(pq, (e.w, e.s, e.t))
while len(pq) != 0:
    w, s, t = heapq.heappop(pq)
    if v[t] == 0:
        v[t] = 1
        dist[t] = w
        ans.append((s, t))
        result += w
        numEdge = numEdge + 1
        for e in G[t]:
            if v[e.t] == 0 and e.w < dist[e.t] :
                dist[e.t] = e.w
                heapq.heappush(pq, (e.w, e.s, e.t))   
if (numEdge == (n-1)):
    print(result)
else:
    print("找不到最小生成樹")
