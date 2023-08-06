# Extract colors using cologram
import turtle
from turtle import Turtle, Screen
import random

# import colorgram
# color = colorgram.extract('hirst.jpg', 30)
# colour_palette = []
# for i in color:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     colour_palette.append(new_color)
# print(colour_palette)

color_list = [(233, 222, 92), (211, 158, 105), (116, 177, 210), (226, 57, 131), (181, 78, 33), (210, 135, 174),
              (41, 103, 161), (12, 21, 62), (184, 46, 111), (186, 164, 23), (43, 182, 112), (122, 187, 155),
              (25, 32, 158), (173, 16, 67), (234, 164, 199), (229, 75, 43), (22, 179, 205), (11, 41, 23), (49, 126, 73),
              (146, 218, 196), (51, 21, 11), (227, 220, 10), (106, 95, 206), (133, 215, 229), (175, 177, 227),
              (59, 16, 31)]

timmy = Turtle()
timmy.penup()
turtle.colormode(255)
# timmy.setheading(225)
# timmy.forward(400)
# timmy.setheading(0)
for i in range(0, 5000, 50):
    timmy.setx(-100)
    timmy.sety(-100 + i)
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

# timmy.dot(20, 'orange')
# timmy.penup()
# timmy.forward(30)

screen = Screen()
screen.exitonclick()
