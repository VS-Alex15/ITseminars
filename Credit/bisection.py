def f(x,a=1,b=0,c=-2,d=0):
    '''
    Многочлен 3-1 стемени
    :аргумент x:
    :1-й коэфф a:
    :2-й коэфф b:
    :3-й коэфф c:
    :свободный член d:
    : return y=f(x):
    '''
    return ((a*x+b)*x+c)*x+d

def bisection(a,b,f,eps=10**(-9)):
    '''
    Поиск корня уравнения f(x)=0
    на интервале [a,b]
    c точностью eps
    return x0, такой что f(x0)=0
    '''
    assert f(a)*f(b)<0
    f_a = f(a)
    f_b = f(b)
    while (b-a)>2*eps:
        tmp=(a+b)/2
        f_t = f(tmp)
        if f_t==0: break
        elif f_t*f_a<0:
            b = tmp
        elif f_t*f_b<0:
            a = tmp
    return tmp

x = bisection(0.5,1.5,f)

print(x)