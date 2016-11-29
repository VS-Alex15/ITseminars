import turtle

def draw(l, n):
    if n==0:
        turtle.forward(l)
        return
    x = l/3
    draw(x,n-1)
    turtle.left(60)
    draw(x,n-1)
    turtle.right(120)
    draw(x, n-1)
    turtle.left(60)
    draw(x,n-1)
n=int(input())
turtle.penup()
turtle.goto(-250,144)
turtle.pendown()
for i in range(3):
    draw(500,n)
    turtle.right(120)
turtle.done()
