import turtle

def draw(l, n):
    if n==0:
        turtle.forward(l)
        return
    x = l/4
    draw(x,n-1)
    turtle.left(90)
    draw(x,n-1)
    turtle.right(90)
    draw(x, n-1)
    turtle.right(90)
    draw(x,n-1)
    draw(x,n-1)
    turtle.left(90)
    draw(x,n-1)
    turtle.left(90)
    draw(x, n-1)
    turtle.right(90)
    draw(x, n-1)
    
n=int(input())
turtle.speed(20)
turtle.penup()
turtle.goto(-150,0)
turtle.pendown()
draw(300,n)
turtle.done()