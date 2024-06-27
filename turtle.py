import turtle
from turtle import Turtle, Screen
import random

game = False
screen = Screen()
screen.setup(width=500, height=500)
bet = screen.textinput(title="Make your bet", prompt='Which turtle will win the race')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70,-40,-10,20,50,80]
tur = []
for index in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colors[index])
    tim.penup()
    tim.goto(x = -230, y =y_pos[index])
    tur.append(tim)

if bet:
    game = True
while game:
    for tu in tur: 
        dist = random.randint(10,20)
        tu.forward(dist)
        if tu.xcor()>230:
            game = False
            winner = tu.pencolor()
            if bet == winner:
                print(f"You won !! {winner} is the winner")
                break
            else:
                print(f"You lost!! {winner} is the winner")
                break




screen.exitonclick()
