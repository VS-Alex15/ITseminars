import turtle as tt
import numpy as np
n = int(input())
tt.shape('turtle')
tt.pendown()
for i in range(n+1):
    tt.left(180-180/n)
    tt.forward(100)
