a = [4, 6, 5, 7, 1, 0, 6, 8, 9, 2]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(a)):
    cnt[a[i]] = cnt[a[i]] + 1
pos[0] = cnt[0]
for i in range(1,10):
    pos[i] = pos[i-1] + cnt[i] 
for i in range(len(a) -1, -1, -1):
    pos[a[i]] = pos[a[i]] - 1
    b[pos[a[i]]] = a[i]
for i in range(len(b)):
    print(b[i], " ", end='')
print()
