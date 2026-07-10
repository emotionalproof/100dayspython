from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

YMAX = 330
XMAX = 600
screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "o")
screen.onkey(paddle2.down, "l")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()
    ball_x = ball.xcor()
    ball_y = ball.ycor()

    if ball_y > YMAX:
        ball.bounce("top")
    elif ball_y < -YMAX:
        ball.bounce("bottom")

    if ball_x > XMAX:
        print("player 1 gets a point")
    elif ball_x < -XMAX:
        print("player 2 gets a point")
    print('ball x: ', ball_x, '|| ball y: ', ball_y)
    print("paddle1y: ", paddle1.middle.ycor(), " || paddle2y: ", paddle2.middle.ycor())
    print("paddle1 distance: ", paddle1.middle.distance(ball), " || paddle2 distance: ", paddle2.middle.distance(ball))
    # if -530 >= ball_x >= -550 and paddle1.top.ycor() >= ball_y >= paddle1.bottom.ycor():
    if -500 >= ball_x >= -600 and paddle1.middle.distance(ball) < 25:
        ball.bounce("left")
    # elif 530 <= ball_x <= 550 and paddle2.top.ycor() >= ball_y >= paddle2.bottom.ycor():
    elif 500 <= ball_x <= 600 and paddle2.middle.distance(ball) < 25:
        print*
        ball.bounce("right")







screen.exitonclick()
