class Kalkulator():



    def __init__(self):
        self.ostatni_wynik = 0


    def dodaj(self, a, b):
        wynik = a+b
        self.ostatni_wynik = wynik
        print(wynik)

    def odejmowanie(self, a, b):
        wynik = a-b
        self.ostatni_wynik = wynik
        print(wynik)

kalk = Kalkulator()
kalk.dodaj(4,4)
kalk.odejmowanie(123,60)
print("ostatni wynik {}".format(kalk.ostatni_wynik))

kalk_2 = Kalkulator()
kalk_2.dodaj(123,54124)
kalk_2.odejmowanie(9,123)
print("ostatni wynik {}".format(kalk_2.ostatni_wynik))

class Rodzic():

    def __init__(self):
        print("Rodzic init")

    def rodzic(self):
        print("rodzic rodzic")

    def poke(self):
        print("rodzic szturnchan")

rodzic = Rodzic()
rodzic.rodzic()
rodzic.poke()

class Dziecko(Rodzic):

    def __init__(self):
        super().__init__()
        print("dziecko init")

    def  poke(self):
        super().poke()
        print("dziecko poked")

dziecko = Dziecko()
dziecko.poke()
dziecko.rodzic()
