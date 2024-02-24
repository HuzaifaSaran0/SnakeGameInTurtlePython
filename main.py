from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game😋")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

N = Snake()
f = Food()
s = Score()
on = True

while on:
    N.Move()
    if N.head.distance(f) < 18:
        f.refresh()
        N.incLength()
        s.scoreInc()

    if N.head.distance(s.bonus) < 20:
        s.scoreInc(inc=5)
        s.bonus.goto(500, 500)

    if int(N.head.heading()) == 0:  # Right side
        screen.onkey(fun=N.left, key="Up")
        screen.onkey(fun=N.right, key="Down")
        screen.onkey(fun=N.nope, key="Left")
        screen.onkey(fun=N.nope, key="Right")
        if N.head.xcor() >= 275.0:  # Adjusted condition
            N.out()
            on = False
            break
    elif int(N.head.heading()) == 90:  # Top side
        screen.onkey(fun=N.left, key="Left")
        screen.onkey(fun=N.right, key="Right")
        screen.onkey(fun=N.nope, key="Up")
        screen.onkey(fun=N.nope, key="Down")
        if N.head.ycor() >= 277:  # Adjusted condition
            N.out()
            on = False
            break
    elif int(N.head.heading()) == 180:  # Left side
        screen.onkey(fun=N.left, key="Down")
        screen.onkey(fun=N.right, key="Up")
        screen.onkey(fun=N.nope, key="Left")
        screen.onkey(fun=N.nope, key="Right")
        if N.head.xcor() <= -277.65:  # Adjusted condition
            N.out()
            on = False
            break
    else:
        screen.onkey(fun=N.left, key="Right")  # Bottom side
        screen.onkey(fun=N.right, key="Left")
        screen.onkey(fun=N.nope, key="Up")
        screen.onkey(fun=N.nope, key="Down")
        if N.head.ycor() <= -275:  # Adjusted condition
            N.out()
            on = False
            break
    for seg in N.turtles[1:]:
        if N.head.distance(seg) < 10:
            on = False
            N.out()


screen.mainloop()
