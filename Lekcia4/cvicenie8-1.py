# python4.pptx -> slide 7

# Vytvorte generator nahodneho textu
# vstupy: ascii OD / ascii DO / dlzka textu
# text by mal obsahova VELKE/MALE PISMENA/Cislice
# MEDZERNIK 32
from random import randint, choices
import string

# 1 sposob, pomocou ascii tabulky
data = input("Vlozte 3 cisla oddelene medzerou (OD DO Dlzka)")
# split()   -> rozdeli retazec na zaklade znaku, ktory dam ako parameter
#              ak na lavej strane je taky pocet premennych, kolko vnikne z retazca tak ich automaticky prideli
gen_from, gen_to, length = data.split(' ')
text = ""
for i in range(int(length)):
    text += chr(randint(int(gen_from), int(gen_to)))
print(text)


# lepsi sposob
length = input("dlzka: ")
# string.ascii_uppercase obashuje vsetky velkepismena, lowercase vsetky male, a digist vsetky cisla
# k -> pocet, kolko vyberov sa ma spravit (parameter funkcie choice())
print(''.join(choices(string.ascii_uppercase + " " + string.ascii_lowercase + string.digits, k=int(length))))
