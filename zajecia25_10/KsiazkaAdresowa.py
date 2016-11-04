class Osoba:
    "...komentarz..."
    nast_nr=1

    def __init__(self):
        self.nr = self.nast_nr
        self.__class__.nast_nr = self.nast_nr + 1
        print 'nr', self.nr
    def dodaj(self):
        self.imie=input("Podaj: \n\t imie")
        self.nazwisko = input("\t nazwisko")
        self.pesel = input("\t pesel")
        self.adres = input("\t adres")
        self.email = input("\t email")
        self.kodpocztowy = input("\t kodpocztowy")
        self.telefon = input("\t telefon")

     def wyswietl(self,nr):

osoba=Osoba()
osoba.dodaj()