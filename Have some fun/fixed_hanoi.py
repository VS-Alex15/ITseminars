def hanoi(n,curr,aim):
    if n==0: return
    else:
        tmp = 6-curr-aim
        if curr==1 and tmp==2:
            hanoi(n-1,curr,tmp)
            hanoi(n-1,tmp,aim)
            print(n,curr,tmp)
            hanoi(n-1,aim,tmp)
            hanoi(n-1,tmp,curr)
            print(n,tmp,aim)
            hanoi(n-1,curr,tmp)
            hanoi(n-1,tmp,aim)
        elif curr==1 and tmp==3:
            hanoi(n-1,curr,aim)
            hanoi(n-1,aim,tmp)
            print(n,curr,aim)
            hanoi(n-1,tmp,aim)
        elif curr==2 and tmp==1:
            hanoi(n-1,curr,tmp)
            print(n,curr,aim)
            hanoi(n-1,tmp,curr)
            hanoi(n-1,curr,aim)
        elif curr==2 and tmp==3:
            hanoi(n-1,curr,tmp)
            print(n,curr,aim)
            hanoi(n-1,tmp,curr)
            hanoi(n-1,curr,aim)
        elif curr==3 and tmp==1:
            hanoi(n-1,curr,aim)
            hanoi(n-1,aim,tmp)
            print(n,curr,aim)
            hanoi(n-1,tmp,aim)
        elif curr==3 and tmp==2:
            hanoi(n-1,curr,tmp)
            hanoi(n-1,tmp,aim)
            print(n,curr,tmp)
            hanoi(n-1,aim,tmp)
            hanoi(n-1,tmp,curr)
            print(n,tmp,aim)
            hanoi(n-1, curr, tmp)
            hanoi(n-1, tmp, aim)

n = int(input())

hanoi(n,1,3)