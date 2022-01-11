import sys
G={}   #使用字典建立圖
for line in sys.stdin:
    n = int(line)
    for i in range(n):
        line=sys.stdin.readline()
        a, b = line.split()
        a = int(a)
        b = int(b)
        if a in G.keys():  #a在字典G內
            G[a].append(b)
        else:              #a不在字典G內
            G[a]=[b]
        if b in G.keys():  #b在字典G內
            G[b].append(a)
        else:              #b不在字典G內
            G[b]=[a]
