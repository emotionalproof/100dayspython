import turtle as t
from turtle import Screen
import random
# 10 x 10 dots
# dots are 20 in size
# spaced apart by 50
# import colorgram

# colors = colorgram.extract('image.jpg', 30)
#
# print(colors)
# rgb_colors = []
# for color in colors:
#     rgb = color.rgb
#     rgb_tuple = (rgb.r, rgb.g, rgb.b)
#     rgb_colors.append((rgb_tuple))
#
# print(rgb_colors)

colors = [(224, 159, 77), (38, 108, 152), (117, 165, 194), (185, 160, 30), (154, 61, 86), (205, 134, 159), (28, 134, 95), (217, 86, 58), (214, 228, 215), (121, 183, 151), (169, 76, 48), (201, 82, 110), (144, 31, 40), (230, 210, 219), (234, 198, 102), (52, 166, 132), (6, 107, 84), (42, 160, 185), (205, 218, 227), (236, 161, 181), (119, 113, 162), (29, 62, 115), (241, 165, 152), (152, 211, 200), (130, 35, 32), (26, 55, 82), (65, 41, 38), (75, 33, 42), (19, 64, 55)]

chip = t.Turtle()
chip.hideturtle()
t.colormode(255)
chip.penup()
row = 0
x = -200
y = -200
chip.speed('fast')
chip.setpos(x, y)
while row < 10:
    y += 50
    chip.goto(x, y)
    for _ in range(10):
        random_color = random.choice(colors)
        chip.dot(20,random_color )
        chip.forward(50)
    row += 1

screen = Screen()
screen.screensize(200, 200)
screen.exitonclick()