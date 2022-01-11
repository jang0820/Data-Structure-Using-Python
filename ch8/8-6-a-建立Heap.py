a=[None, 55, 45, 89, 35, 65, 99, 23, 79]
def max_heapify(h, n, x):
    if (2*x+1) <= n:
        if h[2*x] > h[2*x+1]:
            max = 2*x
        else:
            max = 2*x+1
    else:
        max = 2*x
    if h[x] < h[max]:
        h[x], h[max] = h[max], h[x]
        if 2*max <= n:
            max_heapify(h, n, max)

def build_max_heap(h, n):
    for i in range(n//2, 0, -1):
        max_heapify(h, n, i)
            
build_max_heap(a, len(a)-1)
print(a)
