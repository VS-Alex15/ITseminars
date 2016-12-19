def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        tmp = a[i]
        j = i-1
        while j>-1 and a[j]>tmp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = tmp

a = [int(x) for x in input().split()]

insertion_sort(a)

print(*a)