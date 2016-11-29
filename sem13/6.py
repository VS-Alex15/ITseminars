import turtle

def draw(n,f):
    if n == 0:
        turtle.forward(1)
        return
    if f==0:
         turtle.right(45)
         draw(n - 1,0)
         turtle.left(90)
         draw(n - 1,1)
         turtle.right(45)
    if f==1:
         turtle.left(45)
         draw(n - 1,0)
         turtle.right(90)
         draw(n - 1,1)
         turtle.left(45)

n = int(input())


turtle.speed(200000)
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
draw(n,0)
turtle.done()