def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a = [int(x) for x in input().split()]

bubble_sort(a)

print(*a)