import turtle as tt
import numpy as np
s = input()
tt.shape('turtle')
tt.pendown()
while s != '0':
    if s == 'l': tt.left(90)
    elif s == 'r': tt.right(90)
    elif s == 'g': tt.forward(50)
    s = input()

