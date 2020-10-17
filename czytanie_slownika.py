slownik = {'John': 27, 'John3':22,'John2':11}

print(slownik)


u = input("co chcesz usunac? ")
if u in slownik:
    uc = int(input("ile chcesz usunac? "))
    if uc <= slownik[u]:
        slownik[u] = slownik[u] - uc
        print(u, "usuniete z listy w ilosci", uc)
        
else:
    print(u, "nie ma na liscie")

print(slownik)