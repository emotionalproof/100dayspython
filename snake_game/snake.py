import turtle
from food import Food

class Snake:
    def __init__(self):
        self.heading = 0
        self.segments = []
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.current_x = 0
        self.current_y = 0
        self.food = Food()
        self.round =

    def create_segment(self, color, position):
        new_segment = turtle.Turtle('square')
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        return new_segment

    def create_snake(self):
        for position in self.starting_positions:
            new_segment = self.create_segment('white', position)
            self.segments.append(new_segment)

    def change_heading_right(self):
        if self.heading != 180:
            self.heading = 0

    def change_heading_up(self):
        if self.heading != 270:
            self.heading = 90

    def change_heading_left(self):
        if self.heading != 0:
            self.heading = 180

    def change_heading_down(self):
        if self.heading != 90:
            self.heading = 270

    def next_position(self):
        step_size = 20
        if self.heading == 180:
            self.current_x -= step_size
        elif self.heading == 0:
            self.current_x += step_size
        elif self.heading == 90:
            self.current_y += step_size
        else:
            self.current_y -= step_size

    def check_coordinates(self):
        self.check_walls()

    def check_walls(self):
        if self.current_x > 300 or self.current_x < -300 or self.current_y > 300 or self.current_y < -300:
            game_is_on = False
            print("You hit the wall")

    def check_self(self):
        for index in range(1, len(self.segments)):
            dot = self.segments[index]
            dot_x = dot.xcor()
            dot_y = dot.ycor()
            if dot_x == self.segments[0].xcor() and dot_y == self.segments[0].ycor():
                game_is_on = False
                print("You hit yourself!")
            # else:
            #     check_target()

    def check_target(self):
        check = self.food.check_target(self.segments)
        if check:
            self.segments.append(check)