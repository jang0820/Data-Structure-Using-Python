A=[0]*5   #宣告
A[0] = 1  #寫入
A[1] = 2
A[2] = 3
A[3] = 4
A[4] = 5
A = [1, 2, 3, 4, 5]
print(A[0])  #讀取
for i in range(5):
    print(A[i], end="")
print()

C = [1, 2, 3, 4, 5]
C.append(0)
for i in range(len(C)-1, 2, -1): # 移動後再插入
    C[i] = C[i-1]
C[2] = 6
print(C)

C = [1, 2, 3, 4, 5]
for i in range(1, 4): # 刪除第2個元素
    C[i] = C[i+1]
C.pop(-1)
print(C)

C = [1, 2, 3, 4, 5]
D = [0]*5
for i in range(len(C)):
    D[i] = C[i]
print(D)
