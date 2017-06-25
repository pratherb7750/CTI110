
# This turtle program to draw a snowflake
#M4LAB2:Snowflake
# June 20, 2017
# Bruce Prather



# display options
import turtle
win = turtle.Screen()
mo = turtle.Turtle()


mo.pensize (4)
mo.pencolor ("blue")
mo.shape ("turtle")


#set accumulator to 0
x = 0
while x < 30:
    
    #this action will repeat for 30 cycles

    mo.forward (150)
    mo.right (120)
    mo.forward (50)
    mo.right (180)
    mo.penup ()
    mo.forward (50)
    mo.pendown ()
    mo.left (60)
    mo.pendown ()
    mo.forward (50)
    mo.right (180)
    mo.penup ()
    mo.forward (50)
    mo. right (120)

    mo.penup ()         
    mo.forward (150)
    mo.pendown ()

    mo.right (6)
    x = x + 1





