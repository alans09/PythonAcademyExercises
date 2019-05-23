# CEZAROVA SIFRA

# vytvorte algoritmus, ktory simuluje cezarovu sifru a pouzije ju na desifrovanie

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
shift = int(input("Zadaj posun: "))

# decrypt
shift = 26 - shift
result = ""
for i in message:
    if i.isupper() and i.isalpha():
        result += chr((ord(i) + shift - 65) % 26 + 65)
    elif i.isalpha():
        result += chr((ord(i) + shift - 97) % 26 + 97)
    else:
        result += i

print(f"Decrypted message: {result}")
