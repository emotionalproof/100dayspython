from turtle import Screen, Turtle
import random
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food



screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.onkey(snake.change_heading_left, "Left")
screen.onkey(snake.change_heading_up, "Up")
screen.onkey(snake.change_heading_down, "Down")
screen.onkey(snake.change_heading_right, "Right")
screen.listen()
print('test')

game_is_on = True


def check_target(segments):
    if food.check_target(segments):
        snake.add_segment()
        scoreboard.score += 1
        print('test')

while snake.alive:
    snake.check_self()
    snake.check_walls()
    check_target( segments=snake.segments)
    screen.update()
    time.sleep(0.1)
    snake.update_positions()
    snake.next_position()
    # game_is_on = snake.check_target()


screen.bye()

print(f"You made it to level {scoreboard.score}!")