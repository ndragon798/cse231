#####################################
# Computer Project #2
#
#
# Turtle
#	Asks for amt of squares
#	Draws Squares using turtle
#	Finishes
#####################################
import turtle
import random

# Picks color randomly using shuffle function.


def pick_color():
    colors = ["blue", "black", "brown", "red", "yellow",
              "green", "orange", "beige", "turquoise", "pink"]
    random.shuffle(colors)
    return colors[0]

# Turtle draws square of desired size.


def draw_square(size):
    turtle.goto(0, 0)
    tcolor = pick_color()
    print(tcolor)
    turtle.color(tcolor)
    turtle.begin_fill()
    turtle.up()
    turtle.forward(size / 2)
    turtle.down()
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.end_fill()


# Ask How Many Squares the would like to draw
sqr_amt = int(input("How many squares would you like to draw: "))
if sqr_amt <= 0:
    print("Error 0 or Neg Number entered")
else:
    while 0 < sqr_amt:
        draw_square(40 * sqr_amt)
        print("Square size :", (40 * sqr_amt))
        sqr_amt = sqr_amt - 1
    turtle.hideturtle()
turtle.bye()

# Questions
# Q1: 1
# Q2: 1
# Q3: 1
# Q4: 7
