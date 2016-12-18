'''Циклический сдвиг чисел
    в массиве влево
'''
list = [int(x) for x in input().split()]

def left_shift(a):
    '''Процедура циклического сдвига
       элементов в непустом массиве влево
    '''
    assert a!=[]
    
    n = len(a)

    tmp = a[0]
    for i in range(n-1):
        a[i] = a[i+1]
    a[n-1] = tmp

left_shift(list)

print(*list)    