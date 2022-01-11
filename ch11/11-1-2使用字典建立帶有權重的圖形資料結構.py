class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w
G={}   #使用字典建立圖，字典的value為list
n = int(input())
for i in range(n):
    a, b, w = input().split()
    a = int(a)
    b = int(b)
    w = int(w)
    e1 = Edge(a, b, w)
    e2 = Edge(b, a, w)
    if a in G.keys():  #a在字典G內
        G[a].append(e1)
    else:              #a不在字典G內
        G[a]=[e1]
    if b in G.keys():  #b在字典G內
        G[b].append(e2)
    else:              #b不在字典G內
        G[b]=[e2]
