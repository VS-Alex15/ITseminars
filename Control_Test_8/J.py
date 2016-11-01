n = int(input())
dict = []
for i in range(n):
    dict.append(str(input()))
    dict[i] = [len(dict[i]), dict[i]]
    dict[i][1] = dict[i][1][::-1] + ' ' + dict[i][1]
dict.sort()
len = 0
for i in range(n):
    if dict[i][0] != len:
        print(dict[i][0])
        len = dict[i][0]
    print(dict[i][1])