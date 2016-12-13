n = int(input())


s = 0
while n>0:
    r = n%36
    n = n//36
    if r==33: s+=1
print(s)