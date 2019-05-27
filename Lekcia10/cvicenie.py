import time

#DU DOPLNIT AJ PRE REKURZIVNE FUNKCIE

def time_it(func):
    def inner(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"CAS TRVANIA: {end-start}")
        return result
    return inner



def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


### ak chceme dekorovat rekurzivnu funkciu, musime vnutit iba 1 zavolanie dekorovanej funkcie
# a to zabezpecime prave tak, ze nedekorujeme funkciu, ale dekorator iba 1x zavolame
# cim vynutime iba 1 (inicialne meranie) a kazdy dalsi rekurzivne volanie funkcie uz bude zakladna
decorated_fib = time_it(fib)
print(decorated_fib(35))

###################



# VYTVORTE DEKORATOR, KTORY ODMERIA CAS
## VYKONANIA FIB()
