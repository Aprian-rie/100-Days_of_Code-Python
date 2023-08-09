from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-150, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, font=FONT, align=ALIGNMENT)

    def calculate_score(self):
        self.level += 1
        self.clear()
        self.update_score()
