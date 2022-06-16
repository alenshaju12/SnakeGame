from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0,270)
        self.hideturtle()
        self.score=0
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))

    def increase(self):
        self.clear()
        self.score+=1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))