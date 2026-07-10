from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed(0)
        self.setheading(225)

    def move(self):
        self.forward(10)

    def bounce(self, side):
        if side == "top" or side == "bottom":
            new_heading = 360 - (self.heading())
            self.setheading(new_heading)
        elif side == "left" and self.heading() <= 180:
            new_heading = 180 - (self.heading())
            self.setheading(new_heading)
        elif side == "right" and self.heading() <= 180:
            new_heading = 180 - (self.heading())
            self.setheading(new_heading)

