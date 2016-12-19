def heap_push(data,H):
    H.append(data)
    i = len(H)-1
    while i>0 and H[(i-1)//2]<H[i]:
        ip = (i-1)//2
        H[i],H[ip] = H[ip],H[i]
        i = (i-1)//2
def heap_pop(H):
    data = H[0]
    tmp = H.pop()
    if len(H)!=0:
        H[0] = tmp
    i = 0
    while i*2+1<len(H):
        il = 2*i+1
        ir = 2*i+2
        j = i
        if H[il]>H[j]:
            j = il
        if (ir<len(H)) and (H[j]<H[ir]):
            j = ir
        if i==j: break
        H[i],H[j] = H[j],H[i]
        i = j
    return data
def heap_sort(a):
    H = []
    for i in range(len(a)):
        heap_push(a[i],H)
    for i in range(len(a)):
        a[i] = heap_pop(H)


a = [int(x) for x in input().split()]

heap_sort(a)

print(*a)
