A=[60,50,44,82,55]
print("排序前")
for item in A:
    print(item,' ', end='')
print()
for i in range(1,5):
    insert = A[i]
    j=i-1
    while j>=0:
        if insert < A[j]:
            A[j+1]=A[j]
        else:
            break
        j = j-1
    A[j+1]=insert
    print("插入排序外層迴圈執行", i ,"次結果為") 
    for item in A:
        print(item,' ', end='')
    print() 
