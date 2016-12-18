numbers = [int(x) for x in input().split()]

def reverse(a):
    '''Обращаяет элемменты
        в массиве a
        (процедура)
    '''
    n = len(a)
    for i in range(n//2):
        a[i],a[n-i-1] = a[n-1-i],a[i]

reverse(numbers)

print(*numbers)
