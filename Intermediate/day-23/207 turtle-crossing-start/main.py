import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect when turtle collides with a car
    for car in car_manager.car_list:
        if car.distance(player1) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Detect when the player reached the other side
    if player1.ycor() > 280:
        player1.reset_position()
        car_manager.level_up()
        scoreboard.calculate_score()


screen.exitonclick()
