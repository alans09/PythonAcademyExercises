# vytvorte funkciu, ktorá overí či vstup z klávesnice je
# platné rodné číslo
# dlzka: 9 znakov pre ludi narodenych do 1.1.1954 -> 3 znaky za lomitkom
# ak ma 9 znakov, nemusi byt delitelne 11
# dlzka: 10 znakov pre ludi narodenych po 1.1.1954 -> 4 znaky za lomitkom
# ak ma 10 znakov, musi byt delitelne 11
# nemoze mat 9 znakov, narodeny po 1.1.1954
import datetime


def rc_validator(rc: str) -> bool:
    """ Function to check validity of personal identifiation number

    :param rc: string
    :return: True or False according to validity of check
    """
    # zadanie bolo, ze vstup je string... ak nieje, vraciame false
    if not isinstance(rc, str):
        return False
    # osetrime lomitko tym, ze ho nahradime prazdnym retazcom
    # skrateny if zapis.. v rodnom_cisle by mali zostat iba cislice
    rodne_cislo = rc.replace("/", "") if "/" in rc else rc
    if rodne_cislo.isnumeric():
        # potrebujeme zistit, ci je dotycny muz alebo zena
        # zeny maju 5 a 6 miesto 0x respektive 1x
        # pripravime si datum, na skontrolovanie ci taky datum existuje
        if rodne_cislo[2] == "5" or rodne_cislo[2] == "6":
            date_to_check = rodne_cislo[:2] + str(int(rodne_cislo[2]) - 5) + rodne_cislo[3:6]
        else:
            date_to_check = rodne_cislo[:6]
        # skusime datum previest na datetime objekt (datum v pythone)
        try:
            if len(rodne_cislo) == 9:
                datetime.datetime.strptime("19"+date_to_check, "%Y%m%d")
            else:
                datetime.datetime.strptime(date_to_check, "%y%m%d")
            # ak je rodne cislo 9 miestne (pred 54 rokom, rovno vraciame true)
            # ak je rodne cislo 10 miestne overime, ci je delitelne 11 a ci je po 1953 roku
            # musime pracovat s predpokladom, ze ak mame 10 miestne a je vyssie ako 2000
            if (len(rodne_cislo) == 9 and int(date_to_check[:2]) < 54) or\
                    (len(rodne_cislo) == 10 and int(rodne_cislo) % 11 == 0):
                return True
        except ValueError:
            return False
    else:
        return False
    return False


if __name__ == "__main__":
    if rc_validator(input("Zadaj rodne cislo: ")):
        print("Rodne cislo je platne!")
    else:
        print("Rodne cislo je neplatne!")
