import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Aprian's Snake Game")
screen.tracer(0)
# starting_positions = [(0,0), (-20,0), (-40,0)]
# for turtle in starting_positions:
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.goto(turtle)
i = 0
segments = []
while i < 3:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=(0 - 20 * i), y=0)
    segments.append(new_turtle)
    i += 1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
