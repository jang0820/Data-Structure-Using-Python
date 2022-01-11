class Point:
    def __init__(self, r, c, dis):
        self.r = r
        self.c = c
        self.dis = dis

def bound(row, col, nr, nc):
    if (((row>0) and (row<=nr)) and ((col>0) and (col<=nc))): return 1
    else: return 0

map=[[0]*101 for i in range(101)]
val=[[0]*101 for i in range(101)]
gor=[0,1,0,-1]
goc=[1,0,-1,0]
myq=[]
line = input()   #輸入列數與行數
r, c = line.split()
r = int(r)
c = int(c)
for i in range(1,r+1):    #輸入地圖
    line = input()
    list = line.split()
    for j in range(c):
        map[i][j+1] = int(list[j])
line = input()   #輸入起始點座標
sr, sc = line.split()
sr=int(sr)
sc=int(sc)
myp = Point(sr, sc, 1)
val[myp.r][myp.c]=1
myq.append(myp)  #將起始點加入佇列
while len(myq)>0:
    nextp=myq[0]
    del myq[0]
    for i in range(4): #在地圖內，且可以走，且未拜訪
        if bound(nextp.r+gor[i],nextp.c+goc[i],r,c) and (map[nextp.r+gor[i]][nextp.c+goc[i]] == 1) and (val[nextp.r+gor[i]][nextp.c+goc[i]] == 0): 
            val[nextp.r+gor[i]][nextp.c+goc[i]] = nextp.dis+1
            tmp = Point(0,0,0)   #產生新的Point
            tmp.r=nextp.r+gor[i]
            tmp.c=nextp.c+goc[i]
            tmp.dis=nextp.dis+1
            myq.append(tmp)

for i in range(r):
    for j in range(c):
        print(val[i+1][j+1], end='')
    print()
