from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scorebaord import Scoreboard
# screen setup

screen=Screen()
screen.setup(width=800, height=400)
screen.bgcolor('black')
screen.title("pong")
screen.tracer(0)
scoreboard=Scoreboard()


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 200 or ball.ycor() <-200:
        ball.bounce_y()
    # detect collison with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() <-320:
        ball.bounce_x()
    # Detect if the ball misses the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if the ball misses the right paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
