from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
right_heading = 0
left_heading = 180
forward = True

# def update_heading(degree):
#     global heading
#     heading = degree
#     tim.setheading(heading)
#


def turn_heading(degree):
    global right_heading
    global left_heading
    right_heading += degree
    left_heading += degree


def turn_turtle():
    if forward:
        tim.setheading(right_heading)
    else:
        tim.setheading(left_heading)


def move_forwards():
    tim.forward(10)


def move_right():
    global forward
    forward = True
    tim.setheading(right_heading)
    move_forwards()


def move_left():
    global forward
    forward = False
    tim.setheading(left_heading)
    move_forwards()


def turn_ccw():
    turn_heading(-10)
    turn_turtle()


def turn_cw():
    turn_heading(10)
    turn_turtle()


def reset_screen():
    screen.resetscreen()
    tim.home()


screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=turn_ccw)
screen.onkey(key="s", fun=turn_cw)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()