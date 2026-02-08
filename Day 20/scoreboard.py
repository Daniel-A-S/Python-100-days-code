from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,360)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            font=("Arial", 18, "normal")
        )
    def game_over_wall(self):
        self.goto(0,0)
        self.write(
            "GAME OVER, YOU HIT A WALL",
            align="center",
            font=("Arial", 18, "normal")
            )

    def game_over_collision_with_yourself(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER, YOU HIT YOURSELF",
            align="center",
            font=("Arial", 18, "normal")
        )
    def increase_score(self):
        self.score+=1
        self.update_score()



        
        
    