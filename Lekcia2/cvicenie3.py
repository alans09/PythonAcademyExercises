#   PYTHON2.pptx -> slide 11 cvicenie (vlavo)
print("Ahoj, ako sa volas? ", end="")
meno = input()
if meno[0].lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Tvoje meno zacina na samohlasku")
else:
    print("Tvoje meno zacina na spoluhlasku")
