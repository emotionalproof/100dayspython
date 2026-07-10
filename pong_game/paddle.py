from turtle import Turtle
PLAYER_1_STARTING_POSITIONS = [(-550, 0), (-550, -20), (-550, -40)]
PLAYER_2_STARTING_POSITIONS = [(530, 0), (530, -20), (530, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.segments = []
        self.create_paddle(player)
        self.top = self.segments[0]
        self.middle = self.segments[1]
        self.bottom = self.segments[2]

    def create_paddle(self, player):
        # positions = []
        if player == 1:
            for position in PLAYER_1_STARTING_POSITIONS:
                self.add_segment(position)
        else:
            for position in PLAYER_2_STARTING_POSITIONS:
                self.add_segment(position)

        # for position in positions:
        #     self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(2,1)
        new_segment.speed("fastest")
        # self.shapesize(stretch_len=2, stretch_wid=2)
        self.segments.append(new_segment)

    def move(self, increment):
        for seg_num in range(len(self.segments)):
            new_x = self.segments[seg_num].xcor()
            new_y = self.segments[seg_num].ycor() + increment
            self.segments[seg_num].goto(new_x, new_y)
        self.top = self.segments[0]
        self.middle = self.segments[1]
        self.bottom = self.segments[2]

    def up(self):
        # self.head.setheading(UP)
        # self.head = self.segments[len(self.segments) - 1]
        y_pos = self.top.ycor()
        if y_pos < 280:
            self.move(MOVE_DISTANCE)

    def down(self):
        # self.head.setheading(DOWN)
        # self.head = self.segments[len(self.segments) - 1]
        y_pos = self.bottom.ycor()
        if y_pos > -280:
            self.move(MOVE_DISTANCE * -1)








