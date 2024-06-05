from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# screen.delay(0)
dots = []
heading = 180
current_y = 0
current_x = 0
length = 3
count = 0
alive = True
target_x = 100
target_y = 100
target = {}

def change_heading_right():
    global heading
    if heading != 180:
        heading = 0


def change_heading_up():
    global heading
    if heading != 270:
        heading = 90


def change_heading_left():
    global heading
    if heading != 0:
        heading = 180


def change_heading_down():
    global heading
    if heading != 90:
        heading = 270


screen.onkey(change_heading_left, "Left")
screen.onkey(change_heading_up, "Up")
screen.onkey(change_heading_down, "Down")
screen.onkey(change_heading_right, "Right")
screen.listen()


def move_target():
    global target
    global target_x
    global target_y
    target_x = random.randint(-265, 265)
    target_y = random.randint(-265, 265)
    new_target = Turtle()
    new_target.penup()
    new_target.hideturtle()
    new_target.teleport(target_x, target_y)
    new_target.showturtle()
    new_target.color("blue")
    new_target.shape("square")

    target = new_target


def next_position():
    global heading
    global current_y
    global current_x
    step_size = 21
    if heading == 180:
        current_x -= step_size
    elif heading == 0:
        current_x += step_size
    elif heading == 90:
        current_y += step_size
    else:
        current_y -= step_size


def create_square():
    turtle_instance = Turtle()
    turtle_instance.penup()
    turtle_instance.hideturtle()
    turtle_instance.shape("square")
    turtle_instance.teleport(current_x, current_y)
    turtle_instance.color("white")
    turtle_instance.showturtle()
    dots.append(turtle_instance)
    check_length()


def check_length():
    global length
    global dots
    if len(dots) >= length:
        index_to_remove = len(dots) - length
        dots[index_to_remove].hideturtle()
    next_position()


def check_walls():
    global alive
    if current_x > 290 or current_x < -280:
        alive = False
    elif current_y > 290 or current_y < -290:
        alive = False
    elif len(dots) >= length:
        check_self()


def check_self():
    global alive
    global length
    first_index = len(dots) - length
    for index in range(first_index, len(dots)):
        dot = dots[index]
        dot_x = dot.xcor()
        dot_y = dot.ycor()
        if dot_x == current_x and dot_y == current_y:
            alive = False
            print(index)
            print(current_x, current_y, dot_x, dot_y)
            print("You hit yourself!")
        else:
            check_target()


def check_target():
    global length
    global target
    x_range = range(current_x - 20, current_x + 20)
    y_range = range(current_y - 20, current_y + 20)
    if target_x in x_range and target_y in y_range:
        length += 1
        target.hideturtle()
        move_target()


def check_coordinates():
    check_walls()


move_target()

while alive:
    check_coordinates()
    create_square()

screen.bye()

print(f"You made it to level {length}!")
