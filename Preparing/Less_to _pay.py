n = int(input())

price_list =[0] + list(map(int,input().split()))

min_list = [price_list[0],price_list[1]] + [None]*(n-1)

for i in range(2,n+1):
    min_list[i] = price_list[i]+min(min_list[i-1],min_list[i-2])

print(min_list[len(min_list)-1])
