a=[60,50,44,82,55,24,99,33]
tmp=[0,0,0,0,0,0,0,0]
def merge(L, M, R):
    left=L
    right=M+1
    i=L
    while (left <= M) and (right <= R):
        if a[left]<a[right]:
            tmp[i]=a[left]
            left = left + 1
        else:
            tmp[i]=a[right]
            right = right + 1
        i = i + 1
    while left<=M:
        tmp[i]=a[left];
        i = i + 1
        left = left + 1
    while right<=R:
        tmp[i]=a[right]
        i = i + 1
        right = right + 1
    for i in range(L, R+1):
        a[i]=tmp[i]

def mergesort(L,R):
    if L < R:
        M=(L+R)//2
        mergesort(L,M)
        mergesort(M+1,R)
        merge(L,M,R)
        print("L=", L, "M=", M," R=",R) 
        for item in a:
            print(item,' ', end='')
        print()

print("排序前")
for item in a:
    print(item,' ', end='')
print()
mergesort(0,7); 
