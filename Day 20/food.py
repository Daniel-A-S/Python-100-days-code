from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-380, 380)
        new_y = random.randint(-380, 380)
        self.goto(new_x, new_y)