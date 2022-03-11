import turtle
from turtle import Screen, Turtle
from time import sleep

screen = Screen()                       # Creating Screen
screen.setup(width=600, height=600)     # Setting screen window size
screen.bgcolor("black")                 # setting fill color of screen
screen.title("My snake game")           # Screen title name will change to given string
screen.tracer(0)                        # Animation will get off

snake_blocks = []
for _ in range(3):
    t = Turtle(shape="square")
    t.color("white")
    t.penup()
    snake_blocks.append(t)

snake_blocks[1].goto(x=-20, y=0)
snake_blocks[2].goto(x=-40, y=0)

game_on = True

while game_on:
    sleep(0.08)
    screen.update()
    for block in snake_blocks:
        block.forward(20)







screen.exitonclick()
