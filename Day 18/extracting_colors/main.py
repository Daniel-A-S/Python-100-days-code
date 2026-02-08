# import colorgram
#
# colors=colorgram.extract('image.jpg',30)
# print(colors)
# rgb_colors=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

import random
from turtle import Turtle,Screen

color_list=[(250, 238, 244), (225, 236, 243), (212, 156, 111), (31, 116, 158), (127, 172, 198), (230, 209, 112), (181, 79, 33), (156, 61, 92), (204, 137, 157), (197, 79, 106), (188, 150, 21), (168, 21, 36), (48, 121, 75), (133, 182, 147), (13, 41, 89), (64, 163, 111), (24, 58, 125), (25, 165, 185), (213, 92, 68), (238, 210, 2), (164, 207, 194), (229, 175, 165), (223, 171, 185), (169, 22, 15), (159, 205, 215), (183, 184, 213), (53, 34, 65), (28, 92, 52)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Move to starting position
tim.setheading(225)
tim.forward(250)
tim.setheading(0)


def draw_in_board():
    for row in range(10):
        for col in range(10):
            tim.dot(20, random.choice(color_list))
            tim.forward(50)
        tim.backward(500)
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)


draw_in_board()


screen.exitonclick()
