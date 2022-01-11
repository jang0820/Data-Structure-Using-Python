a = [454, 65, 447, 130, 33, 998, 681, 542, 249]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def dig(x, m):
    x = x % m
    return int(x // (m/10))

def radix_sort(n, k): #n個數值，數值最大為k位數
    for j in range(1, k+1):
        cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m = 10 ** j
        for i in range(n):  #計算數字個數
            x = dig(a[i], m)
            cnt[x] = cnt[x] + 1
        pos[0] = cnt[0]       #累加數字個數
        for i in range(1,10):
            pos[i] = pos[i-1] + cnt[i] 
        for i in range(n-1, -1, -1): #填入
            x = dig(a[i], m) 
            pos[x] = pos[x] - 1
            b[pos[x]] = a[i]
        for i in range(n):  #拷貝
            a[i] = b[i]
        for i in range(n):
            print(a[i], ' ', end='')
        print()
        
radix_sort(9, 3)
