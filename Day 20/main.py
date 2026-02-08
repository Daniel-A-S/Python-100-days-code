from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# setup

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

# ------------------ MOVEMENT ------------------

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# ------------------ GAME LOOP ------------------

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    #  movement
    snake.move()
    # DETECT IF A FOOD IS EATEN
    if snake.head.distance(food) < 15:
        # move the food to a new location
        food.refresh()
        # ADD Body
        snake.add_segment()
        # ADD score
        scoreboard.increase_score()
        # check for wall collision
    if snake.wall_collision():
        game_is_on = False
        print("GAME OVER: Hit the wall")
        scoreboard.game_over_wall()
    if snake.body_collision():
        game_is_on = False
        print("GAME OVER: Hit yourself")
        scoreboard.game_over_collision_with_yourself()
screen.exitonclick()






















