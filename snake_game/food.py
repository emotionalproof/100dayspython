import snake
import random
from turtle import Turtle

class Food:
    def __init__(self):
        self.target = self.create_food()
        # self.x_cor = 600
        # self.y_cor = 600

    def create_food(self):
        new_segment = Turtle('square')
        new_segment.color('blue')
        new_segment.penup()
        new_segment.goto(100, 100)
        # self.x_cor = new_segment.xcor()
        # self.y_cor = new_segment.ycor()
        print(new_segment)
        return new_segment

    def move_target(self):
        target_x = random.randint(-265, 265)
        target_x = target_x - (target_x % 20)
        target_y = random.randint(-265, 265)
        target_y = target_y - (target_y % 20)
        self.target.goto(target_x, target_y)

    def check_target(self, segments):
        if self.target.xcor() == segments[0].xcor() and self.target.ycor() == segments[0].ycor():
            self.move_target()
            return True
        else:
            return False


