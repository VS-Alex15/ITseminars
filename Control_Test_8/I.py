n=int(input())
student=[]
for i in range(n):
    student.append(list(map(float,input().split())))
student.sort(key= lambda g:g[0],reverse=True)
student.sort(key= lambda g:g[1])
for i in range(n):
    p=[str("%.2f" % student[i][0]),str("%.3f" % student[i][1])]
    print(' '.join(p))