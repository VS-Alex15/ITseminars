x = int(input())
a = [int(x) for x in input().split()]
a.sort()

def bin_search(x,a):
    l = 0
    r = len(a)-1
    k = -1
    while l<r:
        m = (l+r)//2
        if a[m]<x:
            l = m+1
        else: r = m
    if a[r]==x:
        return r
    else: return k
print(bin_search(x,a))