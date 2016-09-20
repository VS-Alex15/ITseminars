import turtle as tt
import numpy as np

tt.shape('turtle')
tt.left(180)
for i in range(100):
    tt.left(180/100)
    tt.forward(1)
tt.penup()
tt.goto(50,-50)
tt.pendown()
for i in range(4):
    tt.forward(50)
    tt.left(120)
