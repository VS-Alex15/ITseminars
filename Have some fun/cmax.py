def next():
    next.seed = (next.seed*513 + 1)%2**18
    return 0 if next.seed == 0 else (next.seed**2%100000 + 1)
next.seed = int(input())

x = next()
m = 9999999999999   # Костыли, но что поделать, не знаю, как максимальное задать
result = []
i = 0
while x != 0:
    if x < m:
        m = x
        result = [i]
    elif x == m:
        result.append(i)
    x = next()
    i += 1
print(*result)