class Vector:
    def __init__(self, coords = '0,0'):
        x,y = coords.split(',')
        self.x = float(x)
        self.y = float(y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

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

n = int(input())

far_point = Vector()

for i in range(n):
    point = Vector(input())
    if abs(point)>abs(far_point):
        far_point = point

print(str(far_point))
