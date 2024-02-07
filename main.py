import turtle

window = turtle.Screen()
window.title('Ping-Pong')
window.setup(850, 650)
window.bgcolor('green')
window.tracer(1)

#left paddle starts here
leftPaddle = turtle.Turtle()
leftPaddle.penup()
leftPaddle.goto(-425, 0)
leftPaddle.pendown()
leftPaddle.speed(0)
leftPaddle.shape('square')
leftPaddle.shapesize(6, 2)
leftPaddle.color('white')
leftPaddle.penup()

#right paddle starts here
rightPaddle = turtle.Turtle()
rightPaddle.penup()
rightPaddle.goto(425, 0)
rightPaddle.pendown()
rightPaddle.speed(0)
rightPaddle.shape('square')
rightPaddle.shapesize(6, 2)
rightPaddle.color('white')
rightPaddle.penup()

#ball starts here
ball = turtle.Turtle()
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5
ball.pendown()
ball.speed(45)
ball.shape('circle')
ball.color('red')
ball.penup()

leftPlayerPoints = 0
rightPlayerPoints = 0

score = turtle.Turtle()
score.color('blue')
score.penup()
score.goto(0, 250)
score.write('Left Player : 0  Right Player: 0',
            align="center",
            font=("Courier", 24, "normal"))
score.hideturtle()


def paddle_L_up():
  # W key pressed
  y = leftPaddle.ycor()
  y = y + 20
  leftPaddle.sety(y)


def paddle_L_down():
  # S key pressed
  y = leftPaddle.ycor()
  y = y - 20
  leftPaddle.sety(y)


def paddle_R_up():
  # up arrow pressed
  y = rightPaddle.ycor()
  y = y + 20  # y+= 20
  rightPaddle.sety(y)


def paddle_R_down():
  # down arrow pressed
  y = rightPaddle.ycor()
  y = y - 20  # y -= 20
  rightPaddle.sety(y)


window.listen()
window.onkeypress(paddle_L_up, "w")
window.onkeypress(paddle_L_down, "s")
window.onkeypress(paddle_R_up, "Up")
window.onkeypress(paddle_R_down, "Down")

while True:
  window.update()
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  # bounce off all edges
  if ball.ycor() > 250:
    ball.sety(250)
    ball.dy = ball.dy * -1  # ball.dy *= -1

  if ball.ycor() < -250:
    ball.sety(-250)
    ball.dy = ball.dy * -1  # ball.dy *= -1

  if ball.xcor() > 425:
    ball.goto(0, 0)
    leftPlayerPoints += 1  # leftPlayerPoints = leftPlayerPoints + 1
    ball.dy *= -1
    score.clear()
    score.write('Left Player : {} Right Player: {}'.format(
        leftPlayerPoints, rightPlayerPoints),
                align="center",
                font=("Courier", 24, "normal"))

  if ball.xcor() < -425:
    ball.goto(0, 0)
    rightPlayerPoints += 1
    ball.dy *= -1
    score.clear()
    score.write('Left Player : {} Right Player: {}'.format(
        leftPlayerPoints, rightPlayerPoints),
                align="center",
                font=("Courier", 24, "normal"))

  # collision of ball and paddles
  if (ball.xcor() > 385
      and ball.xcor() < 395) and (ball.ycor() < rightPaddle.ycor() + 40
                                  and ball.ycor() > rightPaddle.ycor() - 40):
    ball.setx(385)
    ball.dx *= -1

  if (ball.xcor() > -395
      and ball.xcor() < -385) and (ball.ycor() < leftPaddle.ycor() + 40
                                   and ball.ycor() > leftPaddle.ycor() - 40):
    ball.setx(-385)
    ball.dx *= -1
