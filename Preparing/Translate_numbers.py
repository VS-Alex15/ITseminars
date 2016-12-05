n = int(input())
A = int(input(),n)
k = int(input())

l = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

'''for i in range(26):
    l.append(chr(ord('A')+i))
'''
def translation(n,a,k):

    s = []
    while a>0:
        r = a%k
        #print(r,end=' ')
        s.append(l[r])
        #print(chr(ord('A')+r-10))
        a = a//k
    s.reverse()
    return s
s = translation(n,A,k)
for i in range(len(s)):
    print(s[i],end='')

