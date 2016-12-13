n, m = list(map(int,input().split()))


cells = [[0]*(m+1) for i in range(n+1) ]

for i in range(n+1):
    cells[i][0] = 1
for i in range(m+1):
    cells[0][i] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        cells[i][j] = cells[i-1][j]+cells[i][j-1]

print(cells[n][m])