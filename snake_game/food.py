import snake
import random
class Food:
    def __init__(self):
        self.target = snake.create_segment('blue', (100, 100))

    def move_target(self):
        target_x = random.randint(-265, 265)
        target_x = target_x - (target_x % 20)
        target_y = random.randint(-265, 265)
        target_y = target_y - (target_y % 20)
        self.target.goto(target_x, target_y)

    def check_target(self, segments):
        if self.target.xcor() == segments[0].xcor() and self.target.ycor() == segments[0].ycor():
            self.move_target()
            last = segments[len(segments) - 1]
            new_segment = snake.create_segment('white', (last.xcor(), last.ycor))
            return new_segment
        else:
            return False


