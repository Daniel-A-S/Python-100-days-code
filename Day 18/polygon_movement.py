import random
from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()
screen.colormode(255)
tim.shape('turtle')


def random_color():
    r=random.randint(0,250)
    g=random.randint(0,250)
    b=random.randint(0,250)
    return (r,g,b)


for sides in range(3,11):
    angle=360/sides
    tim.color(random_color())
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)



screen.exitonclick()
