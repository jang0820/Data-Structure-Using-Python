from heapq import *
hf = [0]*101
code = [0]*10
def dfs(id, level):
    if hf[id][3] == False:
        code[level] = '0'
        dfs(hf[id][4],level+1)
        code[level] = '1'
        dfs(hf[id][5],level+1)
    else:
        print(hf[id][2], " ", end='')
        for i in range(level):
            print(code[i], end='')
        print()
c = ['a', 'b', 'c', 'd', 'e']
w = [10, 4, 5, 7, 8]
pq = []
for i in range(len(c)):
    node = (w[i], i, c[i], True, 0, 0)
    hf[i] = node
    heappush(pq, node)
num = len(c)
while(len(pq) > 1):
    a = heappop(pq)
    b = heappop(pq)
    node = (a[0]+b[0], num, None, False, a[1], b[1])
    hf[num] = node
    heappush(pq, node)
    num = num + 1
dfs(pq[0][1], 0)
