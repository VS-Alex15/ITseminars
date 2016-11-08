class Vector:
    def __init__(self, coords = '0,0'):
        x,y = coords.split(',')
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other):
        return Vector(str(self.x + other.x)+','+ str(self.y + other.y))

    def __iadd__(self, other):
        return Vector(str(self.x + other.x)+','+ str(self.y + other.y))

    def __sub__(self, other):
        return Vector(str(self.x - other.x)+','+ str(self.y - other.y))

    def __isub__(self, other):
        return Vector(str(self.x - other.x)+','+ str(self.y - other.y))

    def __mul__(self, other):            #скалярное произведение
        return (self.x*other.x+self.y*other.y)

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        if not(self.x==other.x and self.y==other.y):
            return True
        else:
            return False

    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def __str__(self):
        return str(self.x)+','+str(self.y)

    def g_vector(self,g):   #умножение вектора на число g (type: float)
        return Vector(str(g*self.x)+','+str(g*self.y))

    def x(self):
        return self.x

    def y(self):
        return self.y


def perimetr(a,b,c):  # рассчет периметра точек с радиус-векторами a,b,c
    assert a!=b and b!=c and a!=c
    return abs(a-b)+abs(b-c)+abs(a-c)

def square(a,b,c):
    p = perimetr(a,b,c)/2
    d1 = abs(a-b)
    d2 = abs(b-c)
    d3 = abs(a-c)
    return (p*(p-d1)*(p-d2)*(p-d3))**0.5

n = int(input())

points = []

for i in range(n):
    points.append(Vector(input()))

S=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            W = square(points[i],points[j],points[k])
            if W>S:
                S = W
if S==0: print('No triangle')
else:
    print(S)