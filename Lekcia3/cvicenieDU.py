year1 = int(input("Zadaj rok od: "))
year2 = int(input("Zadaj rok do: "))
leap_years = [i for i in range(year1, year2+1) if (i % 100 != 0 and i % 4 == 0) or (i % 400 == 0)]
print(f"Prestupne: {' '.join(str(x) for x in leap_years)}") if leap_years\
    else print("Ani 1 rok v rozsahu nieje prestupny")

