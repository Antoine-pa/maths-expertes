from turtle import *
from math import pi

n = int(input("équation de type z^n=1 n : "))
    
reset()
up()
goto(0, -300)
down()
circle(300)
up()
goto(300, 0)

for k in range(n):
    angle_degree = ((2*k*pi)/n)*180/pi
    up()
    goto(0, 0)
    setheading(angle_degree)
    
    