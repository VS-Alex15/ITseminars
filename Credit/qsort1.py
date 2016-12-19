def qsort(a):
    if len(a)<=1:
        return a[:]
    edge = a[len(a)//2]
    L = []
    R = []
    M = []
    for x in a:
        if x<edge:
            L.append(x)
        elif x>edge:
            R.append(x)
        else:
            M.append(x)
    return qsort(L)+M+qsort(R)

a = [int(x) for x in input().split()]

a = qsort(a)

print(*a)