n = int(input())

customer = [[3601]*3 for i in range(3)]
for i in range(n):
    customer.append(list(map(int, input().split())))

x = [0,0,0]

for i in range(3,n+3):
    a=[x[i-1]+customer[i][0]]+[x[i-2]+customer[i-1][1]]+[x[i-3]+customer[i-2][2]]
    x.append(min(a))

print(x[n+2])