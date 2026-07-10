from snake import Snake


class Food(Snake):
    def __init__(self):
        super().__init__()
        self.target = self.create_segment(coordinates=(100,100), color='blue')

