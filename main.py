from turtle import Screen, Turtle
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()                       # Creating Screen
screen.setup(width=600, height=600)     # Setting screen window size
screen.bgcolor("black")                 # setting fill color of screen
screen.title("My snake game")           # Screen title name will change to given string
screen.tracer(0)                        # Animation will get off
snake = Snake()
food = Food()
score = Score()


game_on = True

# start listening to keyboard input on
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    screen.update()
    sleep(0.08)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        score.score_update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()


screen.exitonclick()
