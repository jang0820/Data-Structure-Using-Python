import sys
G={}   #使用字典建立圖
City={}
v=[0]*27
isLoop = False
def getCityIndex(p):  #字串轉編號
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
def DFS(x,start):  #DFS找尋
    global isLoop  #存取全域變數isLoop
    if x in G.keys():  #需判斷x是否是G的鍵值
        for target in G[x]:
            if target == start:
                isLoop = True
                return
            if v[target] == 1:  continue
            v[target] = 1
            DFS(target, start)
            v[target] = 0

for line in sys.stdin:
    G.clear()
    v=[0]*27
    n = int(line)
    for i in range(n):
        a, b = input().split()
        a=getCityIndex(a)  #將a轉成數字
        b=getCityIndex(b)  #將b轉成數字
        if a in G.keys():  #a在字典G內 
            G[a].append(b)
        else:              #a不在字典G內
            G[a]=[b]
    for item in G.keys():
        DFS(item,item)
        if isLoop: break
    if isLoop: print("形成循環")
    else: print("沒有形成循環")
