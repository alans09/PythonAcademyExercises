# Otvoríme súbor data.txt nachádzajúci sa v repozitári v „Lekcia10“
# 1) Spočítame počet slov v tomto súbore (chcem vidieť na obrazovke)
# 2) Zistíme, ktorá samohláska sa najčastejšie vyskytuje (chcem vidieť na obrazovke)
# 3) Vytvoríme nový súbor “samohlasky.txt“ a zapíšeme do neho:
# samohlaska		pocet
# A			<xy>
# E			<ab>
### pohrajte sa s formatovanim suboru, pouzijete f-stringy

fh = open("data.txt", "r")
subor = fh.read()
fh.close()
samohlasky = {}
for znak in subor:
    if znak.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
        if znak in samohlasky.keys():
            samohlasky[znak] = samohlasky[znak]+1
        else:
            samohlasky[znak] = 1

max_key = ""
max_value = 0
# for k in samohlasky:
#     if max_value < samohlasky[k]:
#         max_value = samohlasky[k]
#         max_key = k

for k, v in samohlasky.items():
    if max_value < v:
        max_value = v
        max_key = k

print(f"Pocet slov: {len(subor.split(' '))}")
print(f"Najcastejsie sa vyskytuje samohlaska: {max_key, max_value}")
file_to_write = open("samohlasky.txt", "w")
file_to_write.write("samohlaska\tpocet\n")
for k, v in samohlasky.items():
    file_to_write.write(f"{k}\t\t\t{v}\n")
file_to_write.close()
