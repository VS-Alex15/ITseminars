def bubble(s1, s2):
    for k in range(1, len(s1)):
        for i in range(0, len(s2)-k):
            if s1[i] > s1[i+1]:
                s1[i], s1[i+1] = s1[i+1], s1[i]
                B[i], B[i+1] = B[i+1], B[i]
                B[i] += 1
                B[i+1] += 1
def bubble_without_counting(s1, s2):
    for k in range(1, len(s1)):
        for i in range(0, len(s1)-k):
            if s1[i] > s1[i+1]:
                s1[i], s1[i+1] = s1[i+1], s1[i]
                s2[i], s2[i+1] = s2[i+1], s2[i]

    s1 = [int(x) for x in input().split()]
s2 = [0]*len(s2)
bubble(s1, s2)
dic = {}
for i in range(len(B)):
    if s1[i] not in dic:
        dic[s1[i]] = B[i]
    else:
        dic[s1[i]] += B[i]
keys = list(dic.keys())
values = list(dic.values())
bubble_without_counting(keys, values)
result = []
for i in range(len(keys)):
    result.append(str(keys[i]) + ':' + str(values[i]))
print(*result)
