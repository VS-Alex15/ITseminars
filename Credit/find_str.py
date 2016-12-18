s = input()
subs = input()

def find(s,subs):
    k = -1
    for i in range(len(s)-len(subs)+1):
        for j in range(len(subs)):
            if s[i+j]!=subs[j]: break
        else:
            k = i
            break

    return k

print(find(s, subs))