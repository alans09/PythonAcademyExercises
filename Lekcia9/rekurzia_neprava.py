import turtle
import time


def spirala(d):
    print(f'volanie spir({d})')
    if d > 100:
        pass     # nerob nič
        print('... trivialny pripad - nerobim nic')
    else:
        t.fd(d)
        t.lt(60)
        print(f'... rekurzivne volam spirala({d+3})')
        spirala(d+3)


def spirala_while(d):
    while d <= 100:
        t.fd(d)
        t.lt(60)
        d = d + 3


if __name__ == "__main__":
    t = turtle.Turtle()
    spirala(20)
    t.reset()
    time.sleep(5)
#    spirala_while(20)
