s = input()
if s.find('.')!=-1: k = '.'
else: k = ''
s = s[:s.find('.')]
a = [0]*len(s)
for i in range(len(s)):
    a[i] = ord(s[i])
a.sort()
for i in range(len(s)):
    print(chr(a[i]), end='')
print(k)
