def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1

get_next.seed = int(input())
x = get_next()
power = dict()
while x != 0:
    if x in power:
        power[x] += 1
    else:
        power[x] = 0
    x = get_next()

keys = sorted(power, key=power.get, reverse=False)
MIN = power[keys[0]]
answer = list()
for i in keys:
    if power[i] == MIN:
        answer.append(i)
    else:
        break
answer.sort()
print(*answer)