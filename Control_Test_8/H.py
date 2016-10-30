n = int(input())
numbers = list(map(int, input().split()))
max = len(str(max(numbers)))
for i in range(n):
    numbers[i] = str(numbers[i])
for i in range(n):
    c = max - len(numbers[i])
    numbers[i] = ['0' * (max - len(numbers[i])) + numbers[i], c]
for i in range(n):
    numbers[i][0] = numbers[i][0][::-1]
numbers.sort()
for i in range(n):
    numbers[i][0] = numbers[i][0][::-1]
for i in range(n-1):
    print(int(numbers[i][0]), end = ' ')
print(int(numbers[n-1][0]))
