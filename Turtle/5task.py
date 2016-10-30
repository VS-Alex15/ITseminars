import turtle as tt
import numpy as np
n = int(input())
tt.shape('turtle')
for i in range(3,n+1):
    tt.penup()
    tt.goto(2*i,-2*i)
    tt.pendown()
    for j in range(i):
        tt.left(360/i)
        tt.forward(i*5)
    tt.penup()
    tt.goto(0,0)