x = input().split()
x[0] = int(x[0],16)
x[1] = int(x[1],16)
a = x[0]^x[1]
print(hex(a)[2:])