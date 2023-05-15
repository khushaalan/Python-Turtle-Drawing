"""
##############################################
@Created on May 2023

@authors: 
1. Khushaalan Arjunan (A190409)
2. Stuart Heng Fu Yu (A189660)
##############################################

Hi, Welcome to our little fun project for Lab 4 using python Turtle module.
As per the requirement of the assignment, we have created seven different functions to draw the seven different components.
(Sun, Mountains, Trees, House, River, Bird and Windmill)
And also there are TWO functions (out of the required 6 function) that make use of the for-statement loop to generate patterns. 
(Mountains and Trees)
We've called these two functions TWICE in the main method to generate more Mountain and Tree patterns in the canvas.

Okay, let's get started. First, we need to import the turtle module. and we need to create a screen and a turtle object. 
We've named the turtle object as 'a'.
We've set the dimension to 1152x648 ratio. 
We've also set the background color to light blue.

Since the center of the canvas is (0,0), all the properties of the Cartesian Plane applies here. Our basic idea is to divide the canvas into 4 quadrants. 
Each quadrant is 576x324. Each quadrant is further divided into 4 quadrants.
The purpose of this is to make it easier to draw the components. The components are drawn in the Components class. 
I declared all the variables in the Module. The variables are the dimensions of the quadrants and the sub-quadrants. 
The variables are used in the Components class to draw the components.

This is 2d matric representation of the quadrants and sub-quadrants:

                    Q2Q2 Q2Q1 # Q1Q2 Q1Q1
                    Q2Q3 Q2Q4 # Q1Q3 Q1Q4
                    #####################
                    Q3Q2 Q3Q1 # Q4Q2 Q4Q1
                    Q3Q3 Q3Q4 # Q4Q3 Q4Q4

Here's the code: 
"""

import turtle,math,cmath

### MODULES
class Module:

    ## SCREEN PROPERTIES
    WIDTH = 1152
    HEIGHT = 648
    CENTER_X = 0
    CENTER_Y = 0 
    ## QUADRANT PROPERTIES
    Q_WIDTH = 576
    Q_HEIGHT = 324
    ## SUB-QUADRANT PROPERTIES
    QQ_WIDTH = 288
    QQ_HEIGHT = 162
    
    ## MOUNTAIN PROPERTIES
    # Since the half of the mountain is a right-angled triangle, we can use the Pythagoras Theorem to find the length of the hypotenuse.
    # The steep up angle is the angle between the hypotenuse and the base of the triangle.
    # The steep down angle is the angle between the hypotenuse and the height of the triangle.
    MOUNTAIN_STEEP_LENGTH = math.sqrt((QQ_HEIGHT-0) ** 2 + (QQ_WIDTH-0) ** 2)
    MOUNTAIN_STEEP_UP_ANGLE = math.degrees(math.atan(QQ_HEIGHT / QQ_WIDTH))
    MOUNTAIN_STEEP_DOWN_ANGLE = (0.25*math.pi) - MOUNTAIN_STEEP_UP_ANGLE

    ## HOUSE ROOF PROPERTIES
    # Since the half of the roof is a right-angled triangle, we can use the Pythagoras Theorem to find the length of the hypotenuse.
    # The steep up angle is the angle between the hypotenuse and the base of the triangle.
    # The steep down angle is the angle between the hypotenuse and the height of the triangle.
    HOUSE_ROOF_LENGTH = math.sqrt(((QQ_HEIGHT/2) ** 2) + ((QQ_WIDTH/2) ** 2))
    HOUSE_ROOF_STEEP_UP_ANGLE = math.degrees(math.atan((QQ_HEIGHT/2) / (QQ_WIDTH/2)))
    HOUSE_ROOF_STEEP_DOWN_ANGLE = (0.25*math.pi) - HOUSE_ROOF_STEEP_UP_ANGLE

    ## QUADRANT FUNCTIONS
    def Q1(a):
        a.fillcolor("skyblue")
        a.begin_fill()
        a.setheading(0)
        a.forward(Module.Q_WIDTH)
        a.setheading(90)
        a.forward(Module.Q_HEIGHT)
        a.setheading(180)
        a.forward(Module.Q_WIDTH)
        a.setheading(270)
        a.forward(Module.Q_HEIGHT)
        a.setheading(0)
        a.end_fill()
        print("Quadrant 1 is Rendered")

    def Q1Q1(a):
        a.fillcolor("red")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.end_fill()
        print("Quadrant 1 -> SubQuadrant 1 is Rendered")

    def Q1Q2(a):
        a.fillcolor("blue")
        a.begin_fill()
        a.pendown()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.end_fill()
        print("Quadrant 1 -> SubQuadrant 2 is Rendered")

    def Q1Q3(a):
        a.fillcolor("pink")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 1 -> SubQuadrant 3 is Rendered")

    def Q1Q4(a):
        a.fillcolor("orange")
        a.begin_fill()
        a.setheading(0)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 1 -> SubQuadrant 4 is Rendered")


    def Q2(a):
        a.fillcolor("skyblue")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.Q_HEIGHT)
        a.setheading(180)
        a.forward(Module.Q_WIDTH)
        a.setheading(270)
        a.forward(Module.Q_HEIGHT)
        a.setheading(0)
        a.forward(Module.Q_WIDTH)
        a.end_fill()
        print("Quadrant 2 is Rendered")

    def Q2Q1(a):
        a.fillcolor("red")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.end_fill()
        print("Quadrant 2 -> SubQuadrant 1 is Rendered")

    def Q2Q2(a):
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.end_fill()
        print("Quadrant 2 -> SubQuadrant 2 is Rendered")

    def Q2Q3(a):
        a.fillcolor("pink")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.end_fill()
        print("Quadrant 2 -> SubQuadrant 3 is Rendered")

    def Q2Q4(a):
        a.fillcolor("orange")
        a.begin_fill()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 2 -> SubQuadrant 4 is Rendered")


    def Q3(a):
        a.fillcolor("skyblue")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.Q_HEIGHT)
        a.setheading(180)
        a.forward(Module.Q_WIDTH)
        a.setheading(90)
        a.forward(Module.Q_HEIGHT)
        a.setheading(0)
        a.forward(Module.Q_WIDTH)
        a.end_fill()
        print("Quadrant 3 is Rendered")

    def Q3Q1(a):
        a.fillcolor("red")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 3 -> SubQuadrant 1 is Rendered")

    def Q3Q2(a):
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(180)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 3 -> SubQuadrant 2 is Rendered")

    def Q3Q3(a):
        a.fillcolor("pink")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.end_fill()
        print("Quadrant 3 -> SubQuadrant 3 is Rendered")

    def Q3Q4(a):
        a.fillcolor("orange")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.end_fill()
        print("Quadrant 3 -> SubQuadrant 4 is Rendered")


    def Q4(a):
        a.fillcolor("skyblue")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.Q_HEIGHT)
        a.setheading(0)
        a.forward(Module.Q_WIDTH)
        a.setheading(90)
        a.forward(Module.Q_HEIGHT)
        a.setheading(180)
        a.forward(Module.Q_WIDTH)
        a.end_fill()
        print("Quadrant 4 is Rendered")

    def Q4Q1(a):
        a.fillcolor("red")
        a.begin_fill()
        a.setheading(0)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 4 -> SubQuadrant 1 is Rendered")

    def Q4Q2(a):
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        print("Quadrant 4 -> SubQuadrant 2 is Rendered")

    def Q4Q3(a):
        a.fillcolor("pink")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.end_fill()
        print("Quadrant 4 -> SubQuadrant 3 is Rendered")

    def Q4Q4(a):
        a.fillcolor("orange")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT*2)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH*2)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT*2)
        a.end_fill()
        a.penup()
        print("Quadrant 4 -> SubQuadrant 4 is Rendered")
    



### COMPONENTS
class Components:

    # 7 COMPONENTS' FUNCTIONS
    def Mountains(a,mountain_pos):
        a.color("green")
        a.penup()
        a.goto(mountain_pos[0],mountain_pos[1])
        a.fillcolor("lightgreen")
        a.begin_fill()
        a.pendown()
        # The slope of the mountain
        for i in range(0,2):
            a.setheading(Module.MOUNTAIN_STEEP_UP_ANGLE)
            a.forward(Module.MOUNTAIN_STEEP_LENGTH)
            a.setheading(Module.MOUNTAIN_STEEP_DOWN_ANGLE)
            a.forward(Module.MOUNTAIN_STEEP_LENGTH)
        a.penup()
        a.goto(Module.Q_WIDTH,Module.QQ_HEIGHT)
        a.pendown()
        a.setheading(180)
        a.forward(Module.QQ_WIDTH*2)
        a.forward(Module.QQ_WIDTH*2)
        a.end_fill()
        a.penup()
        a.goto(Module.CENTER_X,Module.CENTER_Y)
        a.color("black")
        print("Mountains are Rendered")


    def Sun(a):
        a.color("orange")
        a.penup()
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(270)
        a.forward(20)
        a.setheading(0)
        a.circle(40,60)
        a.pendown()
        a.circle(40,15)
        a.fillcolor("yellow")
        a.begin_fill()
        a.circle(40,215)
        a.penup()
        a.goto(0,Module.QQ_HEIGHT)
        a.pendown()
        a.setheading(0)
        a.forward(-a.pos()[0])
        a.forward(40)
        a.end_fill()
        a.penup()
        a.goto(0,0)
        a.color("black")
        print("Sun is Rendered")


    def Trees(a,pos,pos2):
        a.penup()
        a.goto(pos[0],pos[1])
        for i in range(0,2):
            a.fillcolor("brown")
            a.begin_fill()
            a.setheading(0)
            a.forward(10)
            a.setheading(270)
            a.forward(60)
            a.setheading(180)
            a.forward(20)
            a.setheading(90)
            a.forward(60)
            a.setheading(0)
            a.forward(10)
            a.end_fill()
            a.penup()
            a.setheading(0)
            a.fillcolor("green")
            a.begin_fill()
            a.circle(35)
            a.end_fill()
            a.penup()
            a.goto(pos2[0],pos2[1])
        print("Trees are Rendered")


    def House(a):
        a.penup()
        a.goto(0,-(Module.QQ_HEIGHT/2))
        a.pendown()
        a.fillcolor("brown")
        a.begin_fill()
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        a.penup()
        # House Roof
        a.goto(0,-(Module.QQ_HEIGHT/2))
        a.pendown()
        a.fillcolor("black")
        a.begin_fill()
        a.setheading(Module.HOUSE_ROOF_STEEP_UP_ANGLE)
        a.forward(Module.HOUSE_ROOF_LENGTH)
        a.setheading(Module.HOUSE_ROOF_STEEP_DOWN_ANGLE)
        a.forward(Module.HOUSE_ROOF_LENGTH)
        a.penup()
        a.goto(Module.QQ_WIDTH,-(Module.QQ_HEIGHT/2))
        a.setheading(180)
        a.forward(Module.QQ_WIDTH)
        a.end_fill()
        a.penup()
        # Door
        a.goto(Module.QQ_WIDTH/2,-((Module.QQ_HEIGHT)+(Module.QQ_HEIGHT/2)-10))
        a.pendown()
        a.fillcolor("black")
        a.begin_fill()
        a.setheading(0)
        a.forward(Module.QQ_WIDTH/8)
        a.setheading(90)
        a.forward(Module.QQ_HEIGHT/2-10)
        a.setheading(180)
        a.forward(Module.QQ_WIDTH/8)
        a.forward(Module.QQ_WIDTH/8)
        a.setheading(270)
        a.forward(Module.QQ_HEIGHT/2-10)
        a.setheading(0)
        a.forward(Module.QQ_WIDTH/8)
        a.end_fill()
        a.penup()
        # Window Left
        a.goto(10,-Module.QQ_HEIGHT)
        a.pendown()
        a.fillcolor("black")
        a.begin_fill()
        a.setheading(90)
        a.forward(20)
        a.setheading(0)
        a.forward(40)
        a.setheading(270)
        a.forward(40)
        a.setheading(180)
        a.forward(40)
        a.setheading(90)
        a.forward(20)
        a.end_fill()
        a.penup()
        # Window Right
        a.goto(Module.QQ_WIDTH-10,-Module.QQ_HEIGHT)
        a.pendown()
        a.fillcolor("black")
        a.begin_fill()
        a.setheading(90)
        a.forward(20)
        a.setheading(180)
        a.forward(40)
        a.setheading(270)
        a.forward(40)
        a.setheading(0)
        a.forward(40)
        a.setheading(90)
        a.forward(20)
        a.end_fill()
        a.penup()
        # Door Knob
        a.goto(((Module.QQ_WIDTH/2)-30) ,-Module.QQ_HEIGHT-40)
        a.pendown()
        a.fillcolor("white")
        a.begin_fill()
        a.setheading(0)
        a.circle(5)
        a.end_fill()
        print("House is Rendered")


    def River(a):
        # River - Hemisphere 1
        a.penup()
        a.goto(-Module.QQ_WIDTH,Module.QQ_HEIGHT)
        a.pendown()
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(180)
        a.circle(Module.QQ_HEIGHT,180)
        a.penup()
        a.setheading(90)
        a.forward(40)
        a.pendown()
        a.setheading(0)
        a.circle(Module.QQ_HEIGHT-40,-180)
        a.end_fill()
        # River - Hemisphere 2
        a.penup()
        a.goto(-Module.QQ_WIDTH,-Module.QQ_HEIGHT+40)
        a.pendown()
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(180)
        a.circle(Module.QQ_HEIGHT,-180)
        a.penup()
        a.setheading(90)
        a.forward(40)
        a.pendown()
        a.setheading(0)
        a.circle(Module.QQ_HEIGHT-40,180)
        a.end_fill()
        # River - Hemisphere 3
        a.penup()
        a.goto(-Module.QQ_WIDTH,Module.QQ_HEIGHT-40)
        a.pendown()
        a.fillcolor("blue")
        a.begin_fill()
        a.setheading(0)
        a.circle(30,90)
        a.setheading(90)
        a.forward(11)
        a.penup()
        a.goto(-Module.QQ_WIDTH+30,Module.QQ_HEIGHT)
        a.setheading(180)
        a.forward(30)
        a.setheading(270)
        a.forward(45)
        a.end_fill()
        print("River is Rendered")


    def Bird(a):
        # Bird 1
        a.penup()
        a.goto(Module.QQ_WIDTH-20,40)
        a.pendown()
        a.setheading(70)
        a.circle(7,180)
        a.penup()
        a.setheading(180)
        a.forward(2)
        a.pendown()
        a.setheading(70)
        a.circle(7,180)
        # Bird 2
        a.penup()
        a.goto(-Module.QQ_WIDTH+30,Module.QQ_HEIGHT+30)
        a.pendown()
        a.setheading(130)
        a.circle(7,180)
        a.penup()
        a.setheading(180)
        a.forward(2)
        a.pendown()
        a.setheading(130)
        a.circle(7,180)
        print("Birds are Rendered")


    def Windmill(a):
        windmill_centre_x = (0.75 * Module.Q_WIDTH)
        windmill_centre_y = (0.75 * Module.Q_HEIGHT - 0.75 * Module.QQ_HEIGHT)
        # Tower
        a.penup()
        a.setheading(0)
        a.goto(windmill_centre_x - 5, windmill_centre_y + 5)
        a.pendown()
        a.fillcolor("wheat")
        a.begin_fill()
        for i in range(2):
            a.forward(10)
            a.right(90)
            a.forward(50)
            a.right(90)
        a.end_fill()
        # Blade
        a.fillcolor("light grey")
        a.penup()
        a.goto(windmill_centre_x, windmill_centre_y)
        a.left(45)
        for i in range(2):
            a.forward(5)
            a.right(90)
            a.pendown()
            a.begin_fill()
            a.forward(30)
            a.right(90)
            a.forward(10)
            a.right(90)
            a.forward(60)
            a.right(90)
            a.forward(10)
            a.right(90)
            a.forward(30)
            a.right(90)
            a.end_fill()
            a.penup()
            a.forward(5)
            a.right(90)
        a.left(135)
        # Centre
        a.fillcolor("white")
        a.penup()
        a.goto(windmill_centre_x, windmill_centre_y - 10)
        a.pendown()
        a.begin_fill()
        a.circle(10)
        a.end_fill()
        print("Windmill is Rendered")


    def Render_Dimensions(a):
        Module.Q1(a)
        Module.Q2(a)
        Module.Q3(a)
        Module.Q4(a)
        Module.Q1Q1(a)
        Module.Q1Q2(a)
        Module.Q1Q3(a)
        Module.Q1Q4(a)
        Module.Q2Q1(a)
        Module.Q2Q2(a)
        Module.Q2Q3(a)
        Module.Q2Q4(a)
        Module.Q3Q1(a)
        Module.Q3Q2(a)
        Module.Q3Q3(a)
        Module.Q3Q4(a)
        Module.Q4Q1(a)
        Module.Q4Q2(a)
        Module.Q4Q3(a)
        Module.Q4Q4(a)


    def Render_Wallpaper(a):
        Module.Q1(a)
        Module.Q2(a)
        Module.Q3(a)
        Module.Q4(a)



"""
Define the screen
Set the title of the screen
Set the dimensions of the working window
We've disabled the resizing of the window because it messes with the Quadrant Dimensions.
The code gets more complex, if we try to fix it and make all the components resize accordingly.
Set the background color of the screen
Define the main drawing function
Initialize the turtle
Set the color of the turtle
Set the width of the turtle
Set the speed of the turtle
Hide the turtle
Print the initial position of the turtle

Render the Dimensions of the Quadrants
Render the Wallpaper - Light Blue

Render the Sun
Render the Mountains (1)
Render the Mountains (2)
Render the Trees (1)
Render the Trees (2)
Render the House
Render the River
Render the Birds
Render the Windmill
Print the final position of the turtle
Print Done

Call the main drawing function
Keep the window open until it is closed manually by clicking on the window
"""



##############################################################################################################
wn = turtle.Screen()
wn.title('A190409_A189660')
wn.setup(width=0.75, height=0.75, startx=None, starty=None)
wn.cv.master.resizable(False, False)
wn.bgcolor("skyblue")

def main_draw():
    print("Initializing and Loading the Canvas...")
    a = turtle.Turtle()
    a.color("black")
    a.width(3)
    a.speed(1000)
    a.hideturtle()
    print("Turle's Initial Position: ", a.position())

    print("Rendering Dimensions...")
    Components.Render_Dimensions(a)
    print("Rendering Wallpaper...")
    Components.Render_Wallpaper(a)

    print("Drawing...")
    Components.Sun(a)
    mountain_pos=(-Module.QQ_WIDTH*2,Module.QQ_HEIGHT)
    Components.Mountains(a,mountain_pos)
    mountain_pos=(mountain_pos[0]-50,mountain_pos[1]-5)
    Components.Mountains(a,mountain_pos)
    pos = (Module.QQ_WIDTH+(Module.QQ_WIDTH/4),-Module.QQ_HEIGHT/2)
    pos2 = (Module.QQ_WIDTH+(Module.QQ_WIDTH/2)+(Module.QQ_WIDTH/4),-((Module.QQ_HEIGHT)+(Module.QQ_HEIGHT/2)))
    Components.Trees(a,pos,pos2)
    pos = (pos[0]+50,pos[1] + 50)
    pos2 = (pos2[0]+50,pos2[1]+50)
    Components.Trees(a,pos,pos2)
    Components.House(a)
    Components.River(a)
    Components.Bird(a)
    Components.Windmill(a)

    print("Turle's Final Position: ", a.position())
    print("Done!")
    
if __name__ == '__main__':
    main_draw()

wn.exitonclick()
##############################################################################################################
