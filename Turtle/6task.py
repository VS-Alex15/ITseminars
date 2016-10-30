import turtle as tt
import numpy as np
n = int(input())
tt.shape('turtle')
tt.pendown()
for i in range(1,n+1):
    for j in range(101):
        tt.left(360/100)
        tt.forward(i*4)
    tt.goto(0,0)
    for j in range(101):
        tt.right(360/100)
        tt.forward(i*4)
    tt.goto(0,0)