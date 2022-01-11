A=[60,50,44,82,55]
print("排序前")
for item in A:
    print(item,' ', end='')
print()
for i in range(4, 0, -1):
    max_index = 0
    for j in range(1, i+1):
        if A[j] > A[max_index]:
            max_index = j
    A[i], A[max_index] =  A[max_index], A[i]
    print("選擇排序外層迴圈執行", 5-i ,"次結果為") 
    for item in A:
        print(item,' ', end='')
    print()
