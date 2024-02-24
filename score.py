import random
import turtle
from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(0, 260)
        self.update_scoreboard()
        self.bonus = Turtle("circle")
        self.bonus.hideturtle()
        self.bonus.goto(500, 500)

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
        self.pen.color("white")

    def scoreInc(self, inc=1):
        self.score += inc
        self.update_scoreboard()
        if self.score > 0 and self.score % 7 == 0:
            self.bonus.showturtle()
            turtle.Screen().tracer(0)
            self.bonus.color("red")
            self.bonus.shapesize(1, 1)
            self.bonus.penup()
            self.bonus.goto(random.randint(0, 255), random.randint(0, 255))
            turtle.Screen().update()
