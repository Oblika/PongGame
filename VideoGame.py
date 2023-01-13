import turtle
import winsound

pn = turtle.Screen()
pn.title("Pong by Samuel Oblika")
pn.bgcolor("black")
pn.setup(width=800, height=600)
pn.tracer(0)

# Score
score_a = 0
score_b = 0


# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("white")
player_a.shapesize(stretch_wid=5, stretch_len=1)
player_a.penup()
player_a.goto(-350, 0)


# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.color("white")
player_b.shapesize(stretch_wid=5, stretch_len=1)
player_b.penup()
player_b.goto(350, 0)

# Paddle UP
paddle_up = turtle.Turtle()
paddle_up.shape("square")
paddle_up.color("white")
paddle_up.goto(0, 300)
paddle_up.shapesize(stretch_wid=0.4, stretch_len=55)


# Paddle Down
paddle_down = turtle.Turtle()
paddle_down.shape("square")
paddle_down.color("white")
paddle_down.goto(0, -292)
paddle_down.shapesize(stretch_wid=0.4, stretch_len=55)

# Start White
paddle_down = turtle.Turtle()
paddle_down.shape("square")
paddle_down.color("white")
paddle_down.goto(0, 15)
paddle_down.shapesize(stretch_wid=4, stretch_len=4)

# Start Black
paddle_down = turtle.Turtle()
paddle_down.shape("square")
paddle_down.color("black")
paddle_down.goto(0, 15)
paddle_down.shapesize(stretch_wid=3.9, stretch_len=3.9)

# Start
paddle_down = turtle.Turtle()
paddle_down.shape("square")
paddle_down.color("white")
paddle_down.goto(0, 15)
paddle_down.shapesize(stretch_wid=0.5, stretch_len=0.5)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Scoreboard
sc = turtle.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))




# Function
def player_a_up():
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_down():
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_b_up():
    y = player_b.ycor()
    y += 20
    player_b.sety(y)

def player_b_down():
    y = player_b.ycor()
    y -= 20
    player_b.sety(y)



# Keyboard binding
pn.listen()
pn.onkeypress(player_a_up, "w")
pn.onkeypress(player_a_down, "s")
pn.onkeypress(player_b_up, "Up")
pn.onkeypress(player_b_down, "Down")




while True:
    pn.update()

    if player_a.ycor() > 250:
        player_a.sety(250)


    if player_a.ycor() < -250:
        player_a.sety(-250)


    if player_b.ycor() > 250:
        player_b.sety(250)


    if player_b.ycor() < -250:
        player_b.sety(-250)




    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("CartoonJump.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("CartoonJump.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sc.clear()
        sc.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sc.clear()
        sc.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    # Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_b.ycor() + 40 and ball.ycor() > player_b.ycor() -40):
         ball.setx(340)
         ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_a.ycor() + 40 and ball.ycor() > player_a.ycor() -40):
         ball.setx(-340)
         ball.dx *= -1




