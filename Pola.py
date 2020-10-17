import figury

from enum import IntEnum

Menu_Figur = IntEnum("Menu", "Kwadrat Prostokat Trojkat Trapez Kolo")
while True:
    
    x = int(input("""
    Witaj w programie do liczenia pola figur
    Napisze prosze co dlajakie figury chcesz obliczyc pole:
            - 1. kwadrat
            - 2. prostokat
            - 3. torjkat
            - 4. trapez
            - 5. kolo"""
                  ))
    if x == Menu_Figur.Kwadrat:
        print("pole kwadratu to:",figury.pole_kwadartu())
    elif x == Menu_Figur.Prostokat:
        print("pole prostokata to:",figury.pole_prostokata())
    elif x == Menu_Figur.Trojkat:
        print("pole trojkat to:",figury.pole_trojkata())
    elif x == Menu_Figur.Trapez:
        print("pole trapezu to:",figury.pole_trapezu())
    elif x == Menu_Figur.Kolo:
        print("pole kola to:",figury.pole_kola(), "policzone razem z PI")
    else:
        print("""
            Nie wybrano figury z listy, wpisz jedno z ponizszych:
            - kwadrat
            - prostokat
            - torjkat
            - trapez
            - kolo""")

