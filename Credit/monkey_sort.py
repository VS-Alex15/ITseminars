from random import shuffle
def monkey_sort(a):
    while not(a==sorted(a)):
        shuffle(a)
    return a

a = [int(x) for x in input().split()]

monkey_sort(a)

print(*a)