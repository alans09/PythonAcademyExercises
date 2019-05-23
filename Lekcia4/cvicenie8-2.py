# python4.pptx -> slide 8

# Vygenerujte nahodny retazec o dlzke 100
# vytvorte zoznam (list), ktory bude obsahovat iba parne cislice z textu
from random import choices
import string

string = (''.join(choices(string.ascii_uppercase + " " + string.ascii_lowercase + string.digits, k=int(100))))
print(string)
####################################################################################################################

list_of_numbers = [int(i) for i in string
                   if (i.isnumeric() and int(i) % 2 == 0)]

# ekvivalenty zapis k list comprehension
# list_of_numbers = []
# for i in string:
#     if i.isnumeric() and int(i) % 2 == 0:
#         list_of_numbers += int(i)


print()
print(f"Vysledok: {list_of_numbers}")

for number in list_of_numbers:
    print(f"{number}", end=" ")
