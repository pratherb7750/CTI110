# This is a turtle program to draw shapes
#M4LAB1: Shapes
# June 20, 2017
# Bruce Prather

# display options
import turtle
win = turtle.Screen()
mo = turtle.Turtle()


mo.pensize (4)
mo.pencolor ("red")
mo.shape ("turtle")

#draw the triangle
x = 0
while x < 3:
    mo.forward (100)
    mo.left (120)
    mo.forward (100)
    x = x+1

mo.penup()

mo.forward (200)

mo.pendown()

#draw the square
x = 0

while x < 4:
    mo.forward (150)
    mo.left (90)
    x = x+1
    
    
    

