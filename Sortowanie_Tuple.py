fhand = open("intro.txt")

# dzielimy caly tesk na linie i slowa + liczymy ile razy sie pojawily

di = dict()
for lin in fhand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) +1

# ukladamy kolejnosc key i value i zamieniamy je na value i key

x = sorted(di.items())
l = list()
for k,v in di.items():
    n = (v,k)
    l.append(n)
l = sorted(l,reverse=True)

# kiedy juz najwieksza wartosc jest ustawiona jako pierwsza, pokazaujemy wynik w kolejnosci, key i value

for v,k in l[:5]:
    print(k,v)
