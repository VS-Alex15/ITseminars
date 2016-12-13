numbers = []
tmp=input()
numbers.append(list(map(int, tmp.split())))
while tmp!='0 0':
    tmp = input()
    numbers.append(list(map(int, tmp.split())))
k = 0
for elem in numbers:
    if elem[0] % 3 != 0 and elem[1]%3 != 0 and elem[0]%5!=0 and elem[1]%5!=0 or (elem[0] > 99 and elem[1] < 100 and elem[1]%2==0) or (elem[1] > 99 and elem[0] < 100 and elem[0]%2==0):
        k+=1
print(k)