from turtle import Turtle
SPEED=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment = []
        self.createsnake()

    def createsnake(self):
        for a in range(3):
            self.addsegment()
            self.one(a)

    def m(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x=self.segment[seg - 1].xcor()
            y=self.segment[seg - 1].ycor()
            self.segment[seg].goto(x,y)

    def move(self):
        self.m()
        self.segment[0].forward(SPEED)

    def left(self):
        if self.segment[0].heading()!=RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading()!=LEFT:
            self.segment[0].setheading(RIGHT)

    def up(self):
        if self.segment[0].heading()!=DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading()!=UP:
            self.segment[0].setheading(DOWN)

    def location(self):
        x = self.segment[0].xcor()
        y = self.segment[0].ycor()
        print(f"{x}x, {y}y snake")
        return (x,y)

    def extend(self):
        self.addsegment()
        self.two()

    def addsegment(self):
        self.tim = Turtle()
        self.tim.color("white")
        self.tim.penup()
        self.tim.shape("square")

    def one(self,a):
        self.tim.setposition(-20 * a, 0)
        self.segment.append(self.tim)
    def two(self):
        self.tim.setposition(self.segment[-1].position())
        self.segment.append(self.tim)