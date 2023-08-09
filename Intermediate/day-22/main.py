import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("PongZ")

screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
pong_ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")

screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move_forward()

    # Detect collision with wall

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # Detect collision with paddle
    if pong_ball.distance(paddle_1) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(paddle_2) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # When the paddle misses the ball(left)
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    # Right paddle misses
    elif pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
