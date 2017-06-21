# This turtle program to draw my initials BP
#M4LAB2:Initials
# June 20, 2017
# Bruce Prather



# display options
import turtle
win = turtle.Screen()
mo = turtle.Turtle()


mo.pensize (4)
mo.pencolor ("red")
mo.shape ("turtle")
#Draw the B
mo.left(90)
mo.forward (150)
mo.right(90)
mo.forward (75)
mo.right (90)
mo.forward (75)
mo.right (90)
mo.forward (75)
mo.right (180)
mo.forward (75)
mo.right(90)
mo.forward (75)
mo.right (90)
mo.forward (75)


#Draw the P
mo.right (180)
mo.penup ()
mo.forward (150)
mo.pendown ()
mo.left(90)
mo.forward (150)
mo.right(90)
mo.forward (75)
mo.right (90)
mo.forward (75)
mo.right (90)
mo.forward (75)


mo.penup ()
mo.forward (206)
mo.right (90)

# mo.forward (200)
mo.pendown ()

x = 0
while x < 360:
    mo.right (1)
    mo.forward (3)
    x = x +1
mo.right (180)
mo.forward (300)
mo.right (90)
mo.forward (75)
mo.right (180)
mo.penup ()
mo.forward (75)
mo.pendown ()
mo.forward (75)

