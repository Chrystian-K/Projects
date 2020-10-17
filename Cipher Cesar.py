# Cesar Cipher

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

x = input(" Co mam zaszyfrowac? ")
n = len(x)
szyfr = ""

for i in range(n):
    litera = x[i]
    if litera.isupper():
        lokalizacja = upper.find(litera)
        nowa_lokalizacja = (lokalizacja + 1) % 26
        szyfr += upper[nowa_lokalizacja]
    else:
        lokalizacja = lower.find(litera)
        nowa_lokalizacja = (lokalizacja + 1) % 26
        szyfr += lower[nowa_lokalizacja]

print(szyfr)