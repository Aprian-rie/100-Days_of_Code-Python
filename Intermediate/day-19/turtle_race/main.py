import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour:")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
all_turtles = []
# for color in colors:
#     timmy = Turtle(shape="turtle")
#     timmy.penup()
#     timmy.color(color)
i = 0
while i < len(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-239, -100 + (i * 40))
    all_turtles.append(new_turtle)
    i += 1

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
