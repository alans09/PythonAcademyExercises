# Ako vstup z klávesnice zadám:
#     počet riadkov
#     počet stĺpcov
#     maximálne a minimálne hodnoty
#
# Výstup budú generované dáta v tvare:
# 1     3     4     5     23
# 23    42    43    211    2
# 23    23    3     4      3
# …
# PYTHON3.pptx -> slide 8 cvicenie
from random import randint
print("Riadky: ", end="")
riadky = input()
print("Stlpce: ", end="")
stlpce = input()
print("MIN: ", end="")
minimum = input()
print("MAX: ", end="")
maximum = input()
print()

for _ in range(int(riadky)):
    for _ in range(int(stlpce)):
        x = randint(int(minimum), int(maximum))
        print(f"{x:^5}", end="")
    print()
