# PYTHON3.pptx -> slide 11 cvicenie
# Napíšte program, ktorý určí či je zadaný (vstup) rok prestupný.
#
# Podmienky:
# 	ak je rok deliteľný 4 a nieje deliteľný 100 => prestupný rok
# 	ak je rok deliteľný 4 a 400 => prestupný rok
# 	všetko ostatné znamená, že rok je neprestupný

print("Zadaj rok: ", end="")
rok = input()

if (int(rok) % 4 == 0 and int(rok) % 100 != 0) or (int(rok) % 4 == 0 and int(rok) % 400 == 0):
    print("PRESTUPNY")
else:
    print("NEPRESTUPNY")


# TODO: Prepiste program tak, ze bude obsahovat podmienky vzdy len s 1 vyrazom
# tj. if (int(rok) % 4 == 0):
#         if (...)...    ziadne kombinovane
