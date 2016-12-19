def merge_sort(a):
    if len(a)<=1:
        return a
    L = merge_sort(a[:len(a)//2])
    R = merge_sort(a[len(a)//2:])
    return merge(L,R)
def merge(a,b):
    i = j = k = 0
    c = [None]*(len(a)+len(b))
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c[k] = a[i]
            i+=1
            k+=1
        else:
            c[k] = b[j]
            j+=1
            k+=1
        c[k:] = a[i:]+b[j:]
    return c

a = [int(x) for x in input().split()]

a = merge_sort(a)
print(*a)
