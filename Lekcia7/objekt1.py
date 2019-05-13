class CvicnaTrieda1:
    premenna1 = "premenna1"

    def funkcia1(self):
        return f"Ahoj, Svet! {self.premenna1}"


class PotomokCvicnejTriedy1(CvicnaTrieda1):
    premenna2 = "potomok - premenna2"

    def funkcia1(self):
        return "Ahoj, Svet z potomka"


if __name__ == "__main__":
    objekt2 = PotomokCvicnejTriedy1()
    print(dir(objekt2))
