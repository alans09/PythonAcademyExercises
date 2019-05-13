class CvicnaTrieda1:
    premenna1 = "premenna1"

    def funkcia1(self):
        return f"Ahoj, Svet! {self.premenna1}"

print(f"__name__: {__name__}")
if __name__ == "__main__":
    objekt1 = CvicnaTrieda1()
    objekt1.premenna1 = "Nova hodnota premennej"
    objekt1.premenna2 = "test"
    print(objekt1.premenna1)
    print(objekt1.premenna2)
    print(objekt1.funkcia1())
