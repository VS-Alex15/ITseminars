def fool_sort(a):
    i = 0
    while i<len(a)-1:
        if a[i]<a[i+1]:
            i+=1
        else:
            a[i],a[i+1] = a[i+1],a[i]
            i = 0

a = [int(x) for x in input().split()]

fool_sort(a)

print(*a)