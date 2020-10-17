from enum import IntEnum

Kolor = IntEnum("kolor", "bialy zloty zielony niebieski czerwony")

while True:

    x = int(input("""
Wybierz dzien tygodnia z listy i zobacz jaki ma kolor:
1. Poniedzialek
2. Wtorek
3. Sroda
4. Czwartek
5. Piatek

"""))
    
    if x == Kolor.bialy:
        print("Poniedzialek ma kolor bialy")

    elif x == Kolor.zloty:
        print("Wtorek ma kolor zloty")

    elif x == Kolor.zielony:
        print("Sroda ma kolor zielony")

    elif x == Kolor.niebieski:
        print("Czwartek ma kolor niebieski")

    elif x == Kolor.czerwony:
        print("Piatek ma kolor czerwony, OGIEN!")

    else:
        print("You made your choice, bye infidel")
        break
        

