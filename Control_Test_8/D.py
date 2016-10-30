price,delta,m = map(int, input().split())
s = 0
day = 1
week = 1
while week<=m:
    s += price
    price += delta
    week = week + day//7
    day =day - 7*(day//7)
    day +=1
print(s)