x = int(input())
a = [int(x) for x in input().split()]

def bin_search(x,a):
    assert a==sorted(a)
    l = 0
    r = len(a)-1
    k = -1
    while r-l>1:
        m = (l+r)//2
        if a[m]<x:
            l = m
        else: r = m
    if a[r]==x:
        return r
    else: return k
print(bin_search(x,a))
