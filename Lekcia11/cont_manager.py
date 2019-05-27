import time
# definujem si Kontext Manager TimeIt
class TimeIt:
    def __init__(self, argument):
        self.arg = argument

    def __enter__(self):
        self.start = time.time()
        return self.arg

    def __exit__(self, *args):
        self.end = time.time()
        print(f"Kontext trval: {self.end - self.start}")


with TimeIt("test") as start_time:
    print(f"START TIME: {start_time}")
    from Lekcia9.fibo import *
    print(fib(35))
print(f"Start mimo kontext: {start_time}")

