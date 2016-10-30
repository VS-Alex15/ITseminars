p=input().strip()
scobki=0
for c in p:
    if c=='(':
        scobki+=1
    if c==')':
        scobki-=1
    if scobki<0:
        break
if (scobki>0) or (scobki<0):
    print('NO')
else:
    print('YES')
