def spocitaj(cislo1: int, cislo2: int) -> int:
    """ Funkcia na spociatenie dvoch cisel.

    :param cislo1: int
    :param cislo2: int
    :return: cislo1+cislo2
    """
    if isinstance(cislo1, int) and isinstance(cislo2, int):
        return cislo1 + cislo2
    else:
        return False


print(f"NAME: {__name__}")


if __name__ == "__main__":
    print("AHOJ SVET")
    print(spocitaj(3, 4))
    print(spocitaj("a", "b"))
