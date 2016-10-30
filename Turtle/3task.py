import turtle as tt
import numpy as np
n = int(input())
tt.shape('turtle')
tt.pendown()
for i in range(n):
    tt.forward(100)
    tt.stamp()
    tt.goto(0,0)
    tt.left(360//n)

