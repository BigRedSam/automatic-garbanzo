import turtle

# set up the turtle screen
win = turtle.Screen()
win.title("Neon Winnie the Pooh")
win.bgcolor("black")

# create a turtle object for drawing
pooh = turtle.Turtle()
pooh.speed(0) # set the drawing speed to the fastest

# set the pen color and fill color
pooh.pencolor("white")
pooh.fillcolor("yellow")

# draw Winnie the Pooh's head
pooh.begin_fill()
pooh.circle(100)
pooh.end_fill()

# draw Winnie the Pooh's ears
pooh.penup()
pooh.setpos(-70, 120)
pooh.pendown()
pooh.begin_fill()
pooh.circle(40)
pooh.end_fill()

pooh.penup()
pooh.setpos(70, 120)
pooh.pendown()
pooh.begin_fill()
pooh.circle(40)
pooh.end_fill()

# draw Winnie the Pooh's eyes
pooh.penup()
pooh.setpos(-40, 40)
pooh.pendown()
pooh.begin_fill()
pooh.circle(20)
pooh.end_fill()

pooh.penup()
pooh.setpos(40, 40)
pooh.pendown()
pooh.begin_fill()
pooh.circle(20)
pooh.end_fill()

# draw Winnie the Pooh's nose
pooh.penup()
pooh.setpos(0, 0)
pooh.pendown()
pooh.pencolor("black")
pooh.fillcolor("red")
pooh.begin_fill()
pooh.circle(10)
pooh.end_fill()

# draw Winnie the Pooh's mouth
pooh.penup()
pooh.setpos(-30, -20)
pooh.pendown()
pooh.pencolor("red")
pooh.width(10)
pooh.setheading(-45)
pooh.circle(50, 90)

# done drawing
turtle.done()
