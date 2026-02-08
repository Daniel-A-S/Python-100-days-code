from turtle import Turtle,Screen


START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_SIZE = 1
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake (self):
        for pos in START_POSITIONS:
            segment =Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            segment.shapesize(SNAKE_SIZE, SNAKE_SIZE)
            self.segments.append(segment)

    def move(self):
            for i in range(len(self.segments) - 1, 0, -1):
                x_new = self.segments[i - 1].xcor()
                y_new = self.segments[i - 1].ycor()
                self.segments[i].goto(x_new, y_new)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].pos())
        new_segment.shapesize(SNAKE_SIZE, SNAKE_SIZE)
        self.segments.append(new_segment)

    def wall_collision(self):
        if self.head.xcor() < -380 or self.head.xcor() > 380 or \
                self.head.ycor() < -380 or self.head.ycor() > 380:
            return True
        else:
            return False

    # ------------------ BODY COLLISION ------------------
    def body_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 15:
                return True
        return False







