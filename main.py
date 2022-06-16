from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameison = True
while gameison:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase()

    #detect collision
    if snake.segment[0].xcor()>290 or snake.segment[0].xcor()<-290 or snake.segment[0].ycor()>290 or snake.segment[0].ycor() <-290:
        gameison=False
        score.gameover()

    #detect tail collision
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)<10:
            gameison = False
            score.gameover()

screen.exitonclick()