# CEZAROVA SIFRA
# python4.pptx -> slide 9
# vytvorte algoritmus, ktory simuluje cezarovu sifru


# Cézarova šifra je druh šifry, pri ktorej je každé písmeno správy posunuté o n pozícií ďalej v abecede,
#     pričom n môže byť 1 až m − 1, kde m je počet znakov príslušnej abecedy
# https://sk.wikipedia.org/wiki/C%C3%A9zarova_%C5%A1ifra
# Anglicka abeceda:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# (+ male pismena)
# pomoc:
#  chr()
#  ord()
#  ascii tabulka
#  .isupper()  <   vrati true (pravda) ak je pismeno/veta velkymi
#  .islower()  <   vrati true (pravda) ak je pismeno/veta malymi pismenami
#  .isalpha()  <   vrati true (pravda) ak je znak pismeno z abeced
message = input("Zadaj vetu: ")
shift = int(input("Zadaj posun (1-26): "))
result = ""

# bez posunu Z -> A / z -> a
for i in message:
    result += chr(ord(i) + int(shift))
    # result = result + chr(ord(i) + int(shift))
print(f"Encrypted message: {result}")

# cezarova sifra nesifruje medzery a specialne znaky!
# upravte sifru, aby medzery vynechavala
# + treba upravit aj to, ze pismeno Z -> A / pismeno z -> a
# vysledok s posunom
result = ""
for i in message:
    if i.isalpha() and i.isupper():
        # ascii A -> 65 , Z -> 90
        if ord(i)+int(shift) > 90:
            result += chr(ord(i) + int(shift) - 26)
        else:
            result += chr(ord(i) + int(shift))
    elif i.isalpha() and i.islower():
        # ascii a -> 97 , z -> 122
        if ord(i)+int(shift) > 122:
            result += chr(ord(i) + int(shift) - 26)
        else:
            result += chr(ord(i) + int(shift))
    else:
        result += i
print(f"Encrypted message: {result}")


# TODO: 1) vytvorte dekryptor  (zadam retazec + posun a vrati mi original)
# TODO: 2) vytvorte BRUTE FORCE dekryptor (zadam retazec a algoritmus zisti, co je v nom napisane)
