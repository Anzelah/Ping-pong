import turtle
import winsound


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
paddle1.shapesize(stretch_wid=3, stretch_len=0.5)
paddle1.color("white")
paddle1.speed(0)

# Create the right paddle
paddle2 = turtle.Turtle()
paddle2.goto(350, 0)
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=3, stretch_len=0.5)
paddle2.color("white")
paddle2.speed(0)

#Create the ball
ball = turtle.Turtle()
ball.goto(0, 0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.dx = 0.5
ball.dy = -0.5

# Functions for moving paddles
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

# Draw the middle line
line = turtle.Turtle()
line.goto(0, 0)
line.shape("square")
line.shapesize(stretch_wid=35, stretch_len=0.02)
line.pendown()
line.color("white")
line.speed(0)

# Initialize scores
playerA = 0
playerB = 0

# Draw the scoreboard
pen = turtle.Turtle()
pen.goto(0, 260)
pen.speed(0)
pen.penup()
pen.color("white")
pen.write("0    0", align="center", font=("Times New Roman", 25, "normal") )
pen.ht()


# Events mainloop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
                                
    # Check the borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = 0.5
        ball.dy = -0.5
        playerA += 1
        pen.clear()
        pen.write("{}    {}".format(playerA, playerB), align="center", font=("Times New Roman", 25, "normal") )
        winsound.PlaySound("Fail.wav", winsound.SND_ASYNC)

    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = 0.5
        ball.dy = -0.5
        playerB += 1
        pen.clear()
        pen.write("{}    {}".format(playerA, playerB), align="center", font=("Times New Roman", 25, "normal") )    
        winsound.PlaySound("Fail.wav", winsound.SND_ASYNC)


    # Ball hitting the paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle2.ycor() +30) and ball.ycor() > (paddle2.ycor() - 30)):
        winsound.PlaySound("Paddle.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.05
        ball.dy *= 1.05
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle1.ycor() +30) and ball.ycor() > (paddle1.ycor() - 30)):
        winsound.PlaySound("Paddle.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.05
        ball.dy *= 1.05
        

















