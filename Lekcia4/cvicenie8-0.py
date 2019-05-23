# Python4.pptx -> slide 5 (zadanie)
number = input("Zadaj cislo:")
number_list = []
while number:
    number = int(number)
    number_list.append(number)
    number = input("Zadaj dalsie cislo:")

print(f" Pocet: {len(number_list)} | {sum(number_list)}")
print(f"{sum(number_list)/len(number_list)}")
print(f"{min(number_list)}")
print(f"{max(number_list)}")
