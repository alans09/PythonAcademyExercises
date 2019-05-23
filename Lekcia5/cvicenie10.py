# spocitanie slov v texte
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


data = str(urllib.request.urlopen(
    "https://raw.githubusercontent.com/alans09/PythonAcademyExercises/master/data.txt"
).read())
text_na_statistiky = data.split(' ')
print(text_na_statistiky)
slovnik = {}
for slovo in text_na_statistiky:  # slovo = "be"
    if slovo in slovnik.keys():
        slovnik[slovo] = slovnik[slovo] + 1
        # slovnik["be"] = slovnik["be"] -> 1 + 1
    else:
        slovnik[slovo] = 1
        # slovnik["be"] = 1

print(slovnik["be"])

