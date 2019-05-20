import turtle
import time
from random import randint, choice

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
farby = ["red", "blue", "white", "cyan", "magenta", "yellow"]
t.shape("turtle")
t.color("blue")
t.fillcolor("red")
while True:
    t.pensize(randint(1, 8))
    t.penup()
    t.setposition(
        randint(-200, 200),
        randint(-200, 200)
    )
    t.pendown()
    t.speed(8)
    t.pencolor(choice(farby))
    # t.pencolor(farby[randint(0, len(farby)-1)])
    for _ in range(4):
        t.left(90)
        t.forward(100)
time.sleep(2)