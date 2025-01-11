from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("Black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.b_move()
    # DETECT COLLISION REBOUND
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # DETECT COLLISION PADDLE
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    # DETECT R MISSES
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    # DETECT L MISSES
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
