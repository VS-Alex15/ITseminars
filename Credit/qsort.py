def qsort(a,l,r):
    i = l
    j = r
    edge = a[(i+j)//2]
    while i<=j:
        while a[i]<edge:
            i+=1
        while a[j]>edge:
            j-=1
        if i<=j:
            a[i],a[j] = a[j],a[i]
    if l<j:
        qsort(a,l,j)
    if i<r:
        qsort(a,i,r)

a = [int(x) for x in input().split()]

qsort(a,0,len(a)-1)

print(*a)