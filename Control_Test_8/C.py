n = int(input())
p = list(map(int, input().split()))
x = [0]*n
k = 0
for i in range(n-1,0,-1):
    x[i-1] = (p[i]^x[i])^1
    k +=x[i-1]
if x[n-1] == (p[0]^x[0])^1:
    print(min(k,n-k))
else: print(0)
