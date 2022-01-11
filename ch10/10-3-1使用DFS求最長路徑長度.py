G={}   #使用字典建立圖
City={}
v=[0]*210
md = 0
def getCityIndex(p):  #字串轉編號
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
def DFS(x,level):  #DFS找尋最深的深度
    global md  #存取第5行全域變數md
    for i in range(len(G[x])):
        if level > md:
            md = level
        target=G[x][i]
        if v[target] == 1:
            continue
        v[target] = 1
        DFS(target,level+1)
m = int(input())
for i in range(m):
    a, b = input().split()
    a = getCityIndex(a)
    b = getCityIndex(b)
    if a in G.keys():  #a在字典G內
        G[a].append(b)
    else:              #a不在字典G內
        G[a]=[b]
    if b in G.keys():  #b在字典G內
        G[b].append(a)
    else:              #b不在字典G內
        G[b]=[a]
start = City[input()]
DFS(start,0)
print(md)
