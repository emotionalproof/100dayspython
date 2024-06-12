from turtle import Screen, Turtle
import random
import time
import snake

snake = snake.Snake()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.onkey(snake.change_heading_left, "Left")
screen.onkey(snake.change_heading_up, "Up")
screen.onkey(snake.change_heading_down, "Down")
screen.onkey(snake.change_heading_right, "Right")
screen.listen()


game_is_on = True














init()


while game_is_on:

    check_self()
    check_walls()
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    next_position()
    segments[0].goto(current_x, current_y)
    check_target()








screen.bye()

print(f"You made it to level {len(segments) - 2}!")