from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=1200, height=640)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
score = Score()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    if ball.distance(r_paddle) < 70 and ball.xcor() == 330 or ball.distance(l_paddle) < 70 and ball.xcor() == -330:
        ball.bounce2()

    if ball.xcor() < -360:
        ball.reset_board()
        score.r_point()

    if ball.xcor() > 360:
        ball.reset_board()
        score.l_point()

screen.exitonclick()
