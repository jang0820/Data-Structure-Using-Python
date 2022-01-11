G=[[0]*100 for i in range(100)]
n = int(input())
for i in range(n):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    G[a][b]=w
    G[b][a]=w
