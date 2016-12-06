n = int(input())


a=[0]*(n+1)

for i in range(n+1):
    a[i] = [0]*(n+1)

for i in range(1,n+1):
    a[i][1] = 1
    a[1][i] = 1
#print(a)
for i in range(2,n+1):
    for j in range(2,n+1):
        if (i==j):
            a[i][j]=a[i][j-1]+1
        elif (i-j)>0:
            a[i][j]=a[i][j-1]+a[i-j][j]
            #print(a[i][j])
            #print(i,j)
            
        else:
            a[i][j]=a[i][j-1]
print(a[n][n])