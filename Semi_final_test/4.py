a = ['c', 's', 'h', 'd']
b = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
sort_rules = []
for i in b:
    for j in a:
        sort_rules.append(i+j)

n = int(input())
s = input()
v = {}
assert len(s)%2 == 0
for i in range(0, len(s), 2):
    stroka = s[i]+s[i+1]
    v.update({sort_rules.index(stroka): stroka})
l = sorted(list(v.keys()))
for i in l:
    print(v[i], end='')