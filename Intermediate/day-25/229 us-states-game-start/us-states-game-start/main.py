# import turtle
import turtle

import pandas
from turtle import Turtle, Screen
# import turtle as turtle
# import turtle as city
screen = Screen()
screen_turtle = Turtle()
city_turtle = Turtle()
# screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen_turtle.shape(image)

is_states_finished = False
states_data = pandas.read_csv("50_states.csv")
# print(states_data)
states_name = states_data["state"]
states_name_list = states_data['state'].to_list()
# print(states_name_list)
state_count = 0
states_already_there = []
states_not_there = []

while not is_states_finished:
    answer_state = screen.textinput(title=f"{state_count} States Correct", prompt="What's another state's name ?")
    title_answer = answer_state.title()
    states_already_there.append(title_answer)
    # print(title_answer)

    # # print(states_name)
    # if answer_state in states_name_list:
    #     t = turtle.Turtle()
    #     t.hideturtle()
    #     t.penup()
    #     t.goto(x=int(states_data[states_data['state'] == title_answer]['x']), y=int(states_data[states_data['state'] == title_answer]['y']))
    #     t.write(title_answer)
    if title_answer == 'Exit':
        break

    for state in states_name_list:
        if title_answer == state and title_answer not in states_already_there:
            city_turtle.penup()
            style = ('Courier', 8, 'normal')
            city_turtle.goto(x=int(states_data[states_data['state'] == title_answer]['x'].iloc[0]),
                             y=int(states_data[states_data['state'] == title_answer]['y'].iloc[0]))
            city_turtle.write(title_answer, font=style)
            city_turtle.hideturtle()
            state_count += 1
    if state_count == 50:
        is_states_finished = True

for all_states in states_name_list:
    if all_states not in states_already_there:
        states_not_there.append(all_states)

states_to_learn_dict = {
    "states to learn": states_not_there
}
states_to_learn = pandas.DataFrame(states_to_learn_dict)

states_to_learn.to_csv("states_to_learn.csv")
