slownik = {}

while True:

    x = input("co chcesz zrobic? wpisze dodaj, usun lub szukaj ")

    if x == "dodaj":
        k = input("co chcesz dodac? ")
        d = input("co to znaczy? ")
        slownik[k] = d
        print(k, "dodane do listy")
        print(slownik)

    elif x == "szukaj":
        s = input("czego szukasz? ")
        if s in slownik:
            print(s, "jest na liscie w ilosci", slownik[s])
        else:
            print(s, "nie ma na liscie")

    elif x == "usun":
        u = input("co chcesz usunac? ")
        if u in slownik:
            print(u, "jest", slownik[u])
            uc = int(input("ile chcesz usunac? "))
            if uc <= int(slownik[u]):
                slownik[u] = int(slownik[u]) - uc
                print(u, "usuniete z listy w ilosci", uc)   
        else:
            print(u, "nie ma na liscie")

    elif x == "zakoncz":
        print("dziekuje, pa pa")
        break



    else:
        print("Nie wybrano popraniwej funkcji, wpisze jeszcze raz")


print(slownik)



