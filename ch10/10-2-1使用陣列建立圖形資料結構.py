import sys
G=[[0]*100 for i in range(100)]
for line in sys.stdin:
    n = int(line)
    for i in range(n):
        a, b = input().split()
        a = int(a)
        b = int(b)
        G[a][b]=1
        G[b][a]=1
