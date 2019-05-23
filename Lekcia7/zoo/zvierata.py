class Zviera:
    popis = None

    def __init__(self, meno, vek, pohlavie):
        self.meno = meno
        self.vek = vek
        self.pohlavie = pohlavie

    def __str__(self):
        raise NotImplementedError("Potrebujes definovat metodu")

    def papanie(self):
        return "ham ham"

    def zvuk(self):
        raise NotImplementedError("Potrebujes definovat zvuk")


class Dingo(Zviera):
    popis = "Australsky skoro pes"

    def __str__(self):
        return f"{self.popis}\nMeno: {self.meno}, Vek: {self.vek}, Pohlavie: {self.pohlavie}"

    def zvuk(self):
        return "vrrr"

if __name__ == "__main__":
    karol = Dingo("Karol", 32, "muzske")
    stefan = Dingo("Stefan", 3, "muzske")
    print(karol.papanie())
    print(karol.zvuk())
    print(karol)
