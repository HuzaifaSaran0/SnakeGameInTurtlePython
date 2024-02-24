import time
from turtle import Turtle, Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        Screen().tracer(0)
        self.penup()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        Screen().update()
        time.sleep(1)

    def refresh(self):
        self.hideturtle()
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
        self.showturtle()
