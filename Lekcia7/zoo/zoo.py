class Zoo:
    otvaracie_hodiny = None
    cennik = None

    def __init__(self, meno, adresa, pavilony=None, obchody=None):
        self.adresa = adresa
        self.meno = meno
        self.pavilony = pavilony
        self.obchody = obchody

    def vstup(self):
        pass

    def krm(self):
        pass

    def zaplat(self):
        pass
