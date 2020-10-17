
print('''
To jest program ktory sumuje Twoje wydatki

Tak dlugo jak bedziesz wpisywac kwote, bedzie sie ona sumowac

Aby zakonczyc kalkulacje wpisz - koniec

''')



b = 0
while True:
    x = input("Ile cie to kosztowalo: ")
    if x == "koniec":
        print("Lacznie wydano: " ,b)
        print("dziekuje i zycze milego dnia ;)")
        break

    b = float(x) + float(b)
    print("Do tej pory wydales wydales: " ,b)


