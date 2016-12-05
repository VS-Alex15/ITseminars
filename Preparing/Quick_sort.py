def quick_sort(a,l,r):
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
            i+=1
            j-=1
    if l<j: quick_sort(a,l,j)
    if i<r: quick_sort(a,i,r)


n = int(input())
a = list(map(int, input().split()))

quick_sort(a,0,n-1)

print(*a)