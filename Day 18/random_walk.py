import random
from turtle import Turtle, Screen

tim= Turtle()
screen = Screen()
screen.colormode(255)
tim.shape('turtle')
tim.speed('fastest')
tim.pensize(10)

def random_color():
    r=random.randint(0,250)
    g=random.randint(0,250)
    b=random.randint(0,250)
    return (r,g,b)

directions=[0,90,180,270]

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

screen.exitonclick()