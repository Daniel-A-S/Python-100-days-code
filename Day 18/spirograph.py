import random
from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()
screen.colormode(255)
tim.shape('turtle')
tim.speed('fastest')


def random_color():
    r=random.randint(0,250)
    g=random.randint(0,250)
    b=random.randint(0,250)
    return (r,g,b)


for angles in range(0,360,10):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(angles)

screen.exitonclick()