import turtle
import time
import random


t = turtle.Turtle()

# t.pencolor("violet")
# t.pensize(10)
# t.speed(2)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.penup()
# t.setposition(random.randint(-100, 100),
#               random.randint(-100, 100))
# t.pendown()
# t.forward(100)
#
#
# t.reset()
# #turtle.tracer(1,0)
# t.shape()
# turtle.bgcolor("black")
#### FIRSt
t2 = turtle.Turtle()
t2.shape("turtle")
wg = turtle.Screen()
wg.bgcolor("black")
while True:
    turtle.tracer(0)
    uhol = random.randint(30, 170)
    uhol2 = random.randint(30, 170)
    t.pensize(random.randint(1,3))
    t2.pensize(random.randint(1,3))
    if uhol > 90:
        t.pencolor("blue")
    else:
        t.pencolor("magenta")
    if uhol2 > 90:
        t2.pencolor("yellow")
    else:
        t2.pencolor("red")
    print(f"UHOL: {uhol}")
    for i in range(3, 500, 5):
        t.forward(i)
        t2.forward(i)
        t.right(uhol)
        t2.right(uhol2)
        turtle.update()
    time.sleep(2)
    t.reset()
    t2.reset()

#### TTT
# turtle.tracer(5,0)
# for uhol in range(10000):
#     t.fd(8)
#     t.rt(uhol+0.8)
# time.sleep(2)
# turtle.update()
