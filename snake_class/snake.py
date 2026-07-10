from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(180)

    def right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(0)

    def up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(90)

    def down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(270)