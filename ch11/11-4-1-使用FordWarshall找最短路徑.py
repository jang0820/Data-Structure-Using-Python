City = {}
G = {}
dis = [[1000000]*100 for i in range(100)]
def getCityIndex(p): 
    if p not in City.keys():
        City[p]=len(City)
    return City[p]
m = int(input())
for i in range(m):
    a, b, w = input().split()
    a=getCityIndex(a)
    b=getCityIndex(b)
    w = int(w)
    dis[a][b] = w
for i in range(len(City)):
    dis[i][i] = 0
for k in range(len(City)):
    for i in range(len(City)):
        for j in range(len(City)):
            if dis[i][k]==1000000 or dis[k][j]==1000000:
                continue
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(len(City)):
    for j in range(len(City)):
        if dis[i][j] == 1000000:
            print("INF", " ", sep="", end="")
        else:
            print(dis[i][j], " ", sep="", end="")
    print()
