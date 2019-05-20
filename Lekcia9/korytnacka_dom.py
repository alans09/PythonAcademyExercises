import turtle
import time
import random


t = turtle.Turtle()
wg = turtle.Screen()
wg.bgcolor("black")
t.reset()
colors = ["white", "red", "blue", "cyan", "orange", "yellow", "magenta", "violet", "lightgreen", "green"]

def draw_house():
    t.color(random.choice(colors))
    t.pensize(5)
    t.speed(2)
    t.left(180)
    t.forward(100)
    t.right(135)
    t.forward(141.4)
    t.left(135)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(30)
    t.forward(100)
    t.right(135)
    t.forward(141.4)
    t.left(135)
    t.forward(100)
    time.sleep(1)

def move_to(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

if __name__ == "__main__":
    while True:
        draw_house()
        move_to(random.randint(-300,300), random.randint(-300,300))
