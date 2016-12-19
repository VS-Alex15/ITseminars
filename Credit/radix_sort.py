def radix_sort(a):
    m = len(str(max(a)))
    for k in range(m):
        b = [[] for x in range(10)]
        for x in a:
            digit = x//10**k%10
            b[digit].append(x)
        a[:] = []
        #for digit in b:
        a[:] = b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]

a = [int(x) for x in input().split()]

radix_sort(a)

print(*a)