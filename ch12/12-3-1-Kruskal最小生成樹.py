import heapq
pq = []
parent = [0]*101
num = [1]*101
def findParent(a):
    while  a!=parent[a]:
        a=parent[a]                  
    return a
n,m = input().split()
n = int(n)
m = int(m)
for i in range(m):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    heapq.heappush(pq, (w, a, b))
for i in range(n):
    parent[i] = i
i = numEdge = result = 0
while i < m and numEdge < n:
    edge = heapq.heappop(pq)
    a=findParent(edge[1]);
    b=findParent(edge[2]);
    if a != b:
        if num[a] > num[b]:
            parent[b]=a
            num[a] += num[b]      
        else:
            parent[a]=b
            num[b]+=num[a]      
        result += edge[0]
        numEdge = numEdge + 1
    i += 1
if (numEdge == (n-1)):
    print(result)
else:
    print("找不到最小生成樹")  
