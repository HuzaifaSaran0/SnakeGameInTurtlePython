import time
from turtle import Turtle, Screen
# ********
# GROUND
# ********
grd = Turtle()
grd.hideturtle()
Screen().tracer(0)
grd.setheading(grd.heading() + 224.2)
grd.fillcolor("red")
grd.penup()
grd.forward(405)
grd.setheading(grd.heading() - 134.2)
grd.pendown()
grd.backward(10)
grd.pencolor("red")
grd.forward(582)
grd.right(90)
grd.forward(580)


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-15, 0), (-30, 0)]
        self.turtles = []
        self.snakeLength = 3
        self.game_over = Turtle()
        self.game_over.hideturtle()
        Screen().tracer(0)
        for part in self.positions:
            self.snake_body(part)
        self.head = self.turtles[0]
        self.head.shape("turtle")

    def snake_body(self, part):
        new_part = Turtle("square")
        new_part.shapesize(0.6, 0.6)
        new_part.penup()
        new_part.color("white")
        new_part.pensize(10)
        new_part.goto(part)
        self.turtles.append(new_part)

    def incLength(self):
        self.snakeLength += 1
        self.snake_body(self.turtles[-1].position())

    def Move(self):
        for segment in range(self.snakeLength - 1, 0, -1):
            x = self.turtles[segment - 1].xcor()
            y = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(x, y)
        self.head.forward(15)
        time.sleep(0.1)
        Screen().update()

    def left(self):
        self.turtles[0].left(90)

    def right(self):
        self.turtles[0].right(90)

    def nope(self):
        pass

    def out(self):
        self.gameOver()
        for T in self.turtles:
            T.color("red")
            Screen().update()

    def gameOver(self):
        self.game_over.color("white")
        self.game_over.write("Game Over", align="center", font=("Arial", 16, "normal"))


if __name__ == "__main__":
    Screen().mainloop()
