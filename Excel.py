plik = input("Wpisz nazwe pliku: ")

try:
    o = open(plik)
except:
    print("file ", plik, " does not exsist")
    quit()


count = 0
for i in plik:
    if not plik.startswith(" "):
        count = count +1
print("W pliku", plik, "jest", count, "lini")


