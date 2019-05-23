# vytvorim slovnik/dictionary  slovnik
slovnik = {"a": 1, "b": 2}
print(slovnik)
# krok 2
slovnik["c"] = 3
print(slovnik)
# krok 3
slovnik["d"] = {"pole": ["ahoj", "svet"]}
print(slovnik)

# vypisat slovo "svet"
print(slovnik["d"]["pole"][1])


print(slovnik.keys())
print(slovnik.values())
