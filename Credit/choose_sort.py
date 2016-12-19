def ch_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
a = [int(x) for x in input().split()]

ch_sort(a)

print(*a)