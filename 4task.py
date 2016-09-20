import turtle as tt
import numpy as np
n = int(input())
tt.shape('turtle')
tt.pendown()
for i in range(2*n,1,-1):
    for j in range(2):
        tt.forward(i*10)
        tt.left(90)
