# import turtle
# keyword: from;
# module name: turtle;
# keyword: import;
# Thing in Module: Turtle

from turtle import Screen
import random
# from turtle import *
# drawback is not being apparent where things in file are coming from
# rare to see in python, not good practice

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    print(color_tuple)
    return color_tuple
# for _ in range(0, 4):
#     tim.color("DeepPink")
#     tim.forward(100)
#     tim.right(90)

# for _ in range(0, 10):
#     tim.pencolor("DeepPink")
#     tim.forward(10)
#     tim.penup()
#     # tim.pencolor("white")
#     tim.forward(10)
#     tim.pendown()


# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)
tim.pensize(1)
# for num in range(3, 11):
#     angle = 360/num
#     tim.pencolor(colors[num - 3])
#     for _ in range(0, num):
#         tim.right(angle)
#         tim.forward(100)

i = 0
tim.speed("fastest")
tim.circle(100)
tim.setheading(0)
size_of_gap = .1
for _ in range(int(360/size_of_gap)):
    tim.pensize(random.randint(0, 30))
    print(tim.heading())
    tim.pencolor(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)
# while i < 1000:
#     tim_heading = 0
#     if i % 10 == 0:
#         print( i)
#
#     direction = random.randint(0,1)
#     angle = random.randint(0, 2) * 90
#     if direction == 0:
#         tim.right(angle)
#         print("right",angle)
#     else:
#         tim.left(angle)
#         print("left", angle)
#     tim.pencolor(random_color())
#     tim.forward(25)
#     i += 1

screen = Screen()
screen.exitonclick()
