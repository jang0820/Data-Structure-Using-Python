score = [-999999, 11, 22, 59, 60, 63, 64, 67, 78, 83, 85, 88, 92]
fib = [0]*100
fib[0] = 0
fib[1] = 1
for i in range(2, 100):
    fib[i] = fib[i-1] + fib[i-2]
def search(key, x):
    y = fib[x]
    while fib[x]>0:
        print("檢查score[", y, "]=", score[y],"是否等於",key)
        if score[y] < key:
            x = x - 1
            y = y + fib[x]
        elif score[y] > key:
            x = x - 1
            y = y - fib[x]
        else:
            break
    if score[y] == key:
        print("找到score[", y, "]=", score[y])
    else:
        print("找不到")
search(59, 5)
