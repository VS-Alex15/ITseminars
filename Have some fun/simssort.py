def double_sort(a, b):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
            if a[j] == a[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
double_sort(s1, s2)
print(*s2)