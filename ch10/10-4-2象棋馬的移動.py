class Point:
    def __init__(self, r, c, step):
        self.r = r
        self.c = c
        self.step = step

def bound(row, col, nr, nc):
    if (((row>0) and (row<=nr)) and ((col>0) and (col<=nc))): return 1
    else: return 0

chess=[[0]*21 for i in range(21)]
gor=[1,-1,-2,-2,-1,1,2,2]
goc=[2,2,1,-1,-2,-2,-1,1]
myq=[]
r, c, sr, sc = input().split()   #輸入棋盤大小與起始點座標
r = int(r)
c = int(c)
sr = int(sr)
sc = int(sc)
chess[sr][sc] = 1
myp = Point(sr, sc, 1)
myq.append(myp)
while len(myq)>0:
    nextp=myq[0]   #貼標籤
    del myq[0]   #根據上一行，nextp仍然可以存取此元素的數值，但myq已經沒有元素了
    for i in range(8):
        if bound(nextp.r+gor[i],nextp.c+goc[i],r,c) and (chess[nextp.r+gor[i]][nextp.c+goc[i]] == 0):
            chess[nextp.r+gor[i]][nextp.c+goc[i]]=nextp.step+1
            tmp = Point(0,0,0)
            tmp.r=nextp.r+gor[i] #不能重複使用myp，因為myp就是myq[0]就是nextp(根據第25與27行)，需要產生新的Point
            tmp.c=nextp.c+goc[i]
            tmp.step=nextp.step+1
            myq.append(tmp)
for i in range(r):
    for j in range(c):
        print(chess[i+1][j+1], end='')
    print()
