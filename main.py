import turtle


# Create your window/screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.title("Simple ping pong game")
wn.tracer(0)

# Create the left paddle
paddle1 = turtle.Turtle()
paddle1.goto(-350, 0)
paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(2.9, 0.5)
paddle1.color("white")
paddle1.speed(0)

# Create the right paddle
paddle2 = turtle.Turtle()
paddle2.goto(350, 0)
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(2.9, 0.5)
paddle2.color("white")
paddle2.speed(0)

#Create the ball
ball = turtle.Turtle()
ball.goto(0, 0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.speed(0)


# Events mainloop
while True:
    wn.update()