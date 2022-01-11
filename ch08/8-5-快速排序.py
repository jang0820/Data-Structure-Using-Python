a=[60,50,44,82,55,47,99,33]
def quicksort(L, R):
    if(L < R) :
        i=L
        j=R+1
        while(1) :
            i=i+1
            while((i < R) and (a[i] < a[L])):
                i=i+1
            j=j-1
            while((j>L) and (a[j]>a[L])):
                j=j-1
            if(i >= j): break
            a[i],a[j] = a[j],a[i]
        a[L],a[j] = a[j],a[L]
        print("L=", L, " j=", j, " R=", R)
        for item in a:
            print(item, ' ', end='')
        print()
        quicksort(L,j-1)
        quicksort(j+1,R)

print("排序前")
for item in a:
    print(item,' ', end='')
print()
quicksort(0,7)
