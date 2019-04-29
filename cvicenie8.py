
print("Zadaj rok: ", end="")
rok = input()

if (int(rok) % 4 == 0 and int(rok) % 100 != 0)\
        or (int(rok) % 4 == 0 and int(rok) % 400 == 0):
        print("PRESTUPNY")
else:
        print("NEPRESTUPNY")

