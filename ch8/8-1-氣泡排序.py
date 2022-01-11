A=[60,90,44,82,50]
print("排序前")
for item in A:
    print(item,' ', end='')
print()
for i in range(len(A)-1,0,-1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
    print("氣泡排序外層迴圈執行第", 5-i ,"次") 
    for item in A:
        print(item,' ', end='')
    print()
