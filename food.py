from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.9)
        self.color("orange")
        self.refresh()
        self.speed("fastest")

    def refresh(self):
        x_coordinates = random.randint(-280, 280)
        y_coordinates = random.randint(-280, 280)
        self.goto(x_coordinates, y_coordinates)
