import turtle
import time


def spirala(d):
    print(f'volanie spir({d})')
    if d > 100:
        print('... trivialny pripad - nerobim nic')
        t.pencolor("blue")
        t.pensize(5)
    else:
        t.fd(d)
        t.lt(60)
        print(f'... rekurzivne volam spirala({d+3})')
        spirala(d+3)
        print(f'... vraciam sa z spirala({d})')
        t.fd(d)
        t.lt(60)


def spirala_while(d):
    pocet = 0
    while d <= 100:
        t.fd(d)
        t.lt(60)
        d = d + 3
        pocet += 1
    t.pencolor("red")
    t.pensize(5)
    while pocet > 0:   # čo sa deje po vynáraní z rekurzie
        d -= 3
        t.fd(d)
        t.lt(60)
        pocet -= 1


if __name__ == "__main__":
    t = turtle.Turtle()
    spirala(20)
    time.sleep(10)
   # spirala_while(20)
