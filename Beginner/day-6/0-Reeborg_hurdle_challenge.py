#Copy the following link the answers is written in the code below
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

##Move in a fixed position
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_in_square():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(0,6):
    move_in_square()
#Using while loop
#no_of_jumps = 6
while no_of_jumps > 0:
    move_in_square()
    no_of_jumps -= 1

