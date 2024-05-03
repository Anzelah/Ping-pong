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


# FUNCTIONS FOR MOVING PADDLES
# Move paddles up and down
def left_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def left_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def right_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def right_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Keybord binding for moving paddles
wn.listen()
wn.onkeypress(left_up, "w")
wn.onkeypress(left_down, "s")
wn.onkeypress(right_up, "Up")
wn.onkeypress(right_down, "Down")


# Events mainloop
while True:
    wn.update()
   