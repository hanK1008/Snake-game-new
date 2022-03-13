from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()                       # Creating Screen
screen.setup(width=600, height=600)     # Setting screen window size
screen.bgcolor("black")                 # setting fill color of screen
screen.title("My snake game")           # Screen title name will change to given string
screen.tracer(0)                        # Animation will get off

snake = Snake()


game_on = True

# start listening to keyboard input on
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

screen.exitonclick()
