import turtle
import math
x , y , radius = eval(input("请输入圆心以及半径"))
turtle.penup()
turtle.goto(x , y - radius)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(x,y)
turtle.write(math.pi*radius**2)
turtle.done()