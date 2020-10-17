import math

def pole_prostokata():
    a = float(input("Podaj dlugość pierwszego boku: "))
    b = float(input("Podaj dlugość drugiego boku: "))
    return a*b

def pole_kwadartu():
    a = float(input("Podaj dlugość pierwszego boku: "))
    b = float(input("Podaj dlugość drugiego boku: "))
    if a == b:
        return a*b
    else:
        print("To nie jest kwadrat! Sproboj jeszcze raz")
        print("")

def pole_trojkata():
    a = float(input("Podaj dlugość pierwszego boku: "))
    b = float(input("Podaj dlugość wyskości: "))
    return 0.5 * a * b

def pole_trapezu():
    a = float(input("Podaj dlugość pierwszego boku: "))
    b = float(input("Podaj dlugość drugiego boku: "))
    c = float(input("Podaj dlugość wysokości boku: "))
    return (a+b) / 2*c

def pole_kola():
    a = float(input("Podaj dlugość promienia: "))
    return math.pi * (a**a)
