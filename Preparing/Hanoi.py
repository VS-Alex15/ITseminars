def hanoi(n,curr,aim):
    if n==1:
        print(n,curr,aim)
    else:
       tmp = 6-curr-aim
       hanoi(n-1,curr,tmp)
       print(n,curr,aim)
       hanoi(n-1,tmp,aim)

n = int(input())
hanoi(n,1,3)