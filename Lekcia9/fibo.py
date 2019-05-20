# Napíšte funkciu na výpočet n-tého člena
# Fibonacciho postupnosti a vypíšte prvých n-členov
# 1, 1, 2, 3, 5, 8, 13, 21, 34 ….

count = 0
cache = {}
def fib(n):
    global count
    global cache
    count += 1
    if n in cache.keys():
        return cache[n]
    if n <= 2:
        return 1
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result


print(fib(40))
print(f"COUNT: {count}")
print(f"CACHE: {cache}")
