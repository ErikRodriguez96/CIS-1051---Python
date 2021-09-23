#Erik Rodriguez - TUID: 915255369
#Section 001
import turtle

print("**Welcome to Turtle Labs**")
bob = turtle
bob.shape("turtle")

def rings():

    bob.pu()
    bob.width(8)

    #blue ring
    bob.goto(-120,0)
    bob.color("blue")
    bob.pd()
    bob.circle(50)
    bob.pu()
    bob.seth(0)

    #yellow ring
    bob.goto(-60,-60)
    bob.color("yellow")
    bob.pd()
    bob.circle(50)
    bob.pu()

    bob.goto(0,0)
    bob.color("black")
    bob.pd()
    bob.circle(50)
    bob.pu()

    bob.goto(60,-60)
    bob.color("green")
    bob.pd()
    bob.circle(50)
    bob.pu()

    bob.goto(120,0)
    bob.color("red")
    bob.pd()
    bob.circle(50)
    bob.pu()

def clock():
    bob.setpos(0,0)

    angles = [0,30,60,90,120,150,180,210,240,270,300,330]

    for x in angles:
        bob.pu()
        bob.seth(x)
        bob.forward(150)
        bob.pd()
        bob.forward(50)
        bob.pu()
        bob.forward(20)
        bob.stamp()
        bob.setpos(0,0)

    bob.hideturtle()

def initials():
    bob.pu()
    bob.pensize(5)
    
    #Drawing E
    bob.setpos(-100,-100)
    bob.pd()
    bob.seth(90)
    bob.forward(200)
    bob.pu()

    bob.setpos(-100,-100)
    bob.pd()
    bob.seth(0)
    bob.forward(100)
    bob.pu()

    bob.setpos(-100,0)
    bob.pd()
    bob.seth(0)
    bob.forward(75)
    bob.pu()

    bob.setpos(-100,100)
    bob.pd()
    bob.seth(0)
    bob.forward(100)
    bob.pu()

    #Drawing R
    bob.setpos(50, -100)
    bob.pd()
    bob.seth(90)
    bob.forward(200)
    
    bob.seth(180)
    bob.circle(50,-180)

    bob.seth(300)
    bob.forward(120)

def givenShape():
    bob.pu()
    bob.pensize(5)

    sides = int(input("Please input the sides of your shape as an integer: "))
    if sides <= 2:
        print("Shape must have more than 2 sides, please try again")
        givenShape()

    angle = int(360 / sides)

    bob.pd()
    for x in range(sides):
        bob.seth(x * angle)
        bob.forward(100)
    bob.hideturtle()

run = True
while (run == True):

    print("(1) - Olympic Rings")
    print("(2) - Clock")
    print("(3) - Initials")
    print("(4) - Shapes")
    print("(5) - EXIT")
    select = int(input("Please enter the integer next to the program you want to run: "))
    bob.reset()             
    if select == 1:
        rings()
    elif select == 2:
        clock()
    elif select == 3:
        initials()
    elif select == 4:
        givenShape()
    elif select == 5:
        print("**Exiting Program**")
        run = False
    else:
        print("That is not a valid selection, please try again")
    print(" ")
                 
