from random import randint
print("Riadky: ", end="")
riadky = input()
print("Stlpce: ", end="")
stlpce = input()
print("MIN: ", end="")
min = input()
print("MAX: ", end="")
max = input()
print()

for _ in range(int(riadky)):
    for _ in range(int(stlpce)):
        x = randint(int(min), int(max))
        print(f"{x:^5}", end="")
    print()

