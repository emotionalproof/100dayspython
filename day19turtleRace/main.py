from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the race!")
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
turtles = []
winner = False
winner_turtle = ""

for i in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.fillcolor(colors[i])
    y_coordinate = 200 - (i * 40) - 100
    turtle.penup()
    turtle.goto(x=-240, y=y_coordinate)
    turtles.append(turtle)


def move_turtle():
    for turtle_racer in turtles:
        steps = random.randint(0, 10)
        turtle_racer.forward(steps)
        global winner
        global winner_turtle
        if turtle_racer.xcor() > 230:
            winner = True
            winner_turtle = turtle_racer.fillcolor()
            break


while not winner:
    move_turtle()

screen.bye()

if user_bet == winner_turtle:
    print("You bet correctly!")
else:
    print(f"You did not bet correctly! {winner_turtle} won, you fool!")

