from functools import lru_cache


# classic fibonacci
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# fibonacci using cache
cache = {}
def fib_cache(n):
    if n in cache.keys():
        return cache[n]
    if n < 2:
        return n
    x = fib(n - 1) + fib(n - 2)
    cache[n] = x
    return x


# fibonacci using build in cache
# least recently used cache
@lru_cache(maxsize=1000)
def fib_lru(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# fibonacci using generator
def fib_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# list comprehension ... vytvaram zoznam s 1000 prvkami
zoznam = [x for x in range(1000)]
print(type(zoznam))
# obdoba list comprehension.. vytvaram generator
generator = (x for x in range(10000))
print(type(generator))



### porovnanie globals a locals
print(f"GLOBALS: {globals()}")
def test_function(a, b):
    print(f"LOCALS: {locals()}")
    return a+b

test_function(1,2)
print (f"test function result:  {test_function(1,2)}")
x = fib_generator(10000)
print(list(x)[-1])
print(x.__next__())

# for i in range(33):
#      print(fib(i+1))
#
# print("------")
# for i in range(33):
#     print(fib_cache(i+1))
#
# print("------")
# for i in range(33):
#     print(fib_lru(i+1))
