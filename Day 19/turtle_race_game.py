from turtle import Turtle, Screen
import random
color=["red","yellow","green","purple","Violet"]


screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="make your bet", prompt= "which turtle will win the race")
tim=Turtle(shape="turtle")
tim.color("red")
tim.penup()
tomy=Turtle(shape="turtle")
tomy.penup()
tomy.color("yellow")
danny=Turtle(shape="turtle")
danny.penup()
danny.color("green")
binny=Turtle(shape="turtle")
binny.color("violet")
binny.penup()

participants=[tim,tomy,danny,binny]


tim.goto(-230,-150)
tomy.goto(-230,-100)
danny.goto(-230,-50)
binny.goto(-230,50)
print(user_bet)

edge_of_Screen=[(230,-150),(230,-100),(230,-50),(230,50)]
speed_limit=(1,60)


def play_game ():
    continue_game=True
    while continue_game:
        def move_forward():
            tim.forward(random.randint(speed_limit[0], speed_limit[1]))
            tomy.forward(random.randint(speed_limit[0], speed_limit[1]))
            danny.forward(random.randint(speed_limit[0], speed_limit[1]))
            binny.forward(random.randint(speed_limit[0], speed_limit[1]))
        move_forward()
        if tim.xcor () >=230 or tomy.xcor()>=230 or danny.xcor()>=230 or binny.xcor()>=230:
            continue_game=False
            for participant in participants:
                if participant.xcor() >=230:
                    winner_color=participant.pencolor()
                    print(f"the winner is {winner_color}")
                    if user_bet==winner_color:
                        print("you win!")
                    else:
                        print("you loose")


play_game()

screen.exitonclick()