import time

def suma_dekorator(func):
    print("Volanie SUMA_DEKORATOR")
    def inner(*args, **kwargs):
        print("Volanie SUMA_DEKORATOR-INNER")
        result = func(*args)
        print("Vraciam novu FUNKCIU")
        return result*2
    return inner

start = time.time()
end = time.time()
print(start - end)

@suma_dekorator
def suma(a, b):
    print("Volanie SUMA")
    return a+b

def sumaC(a, b):
    return a+b

print(suma(1, 5))

# suma_decorated = suma_dekorator(suma)
# print(suma_decorated(1, 5))


