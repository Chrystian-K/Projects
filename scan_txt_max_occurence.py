fname = input("nazwa pliku: ")
if len(fname) <1 : fname = "clown.txt"

hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()

    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) +1


l = -1
s = None
for k,v in di.items():
    if v > l:
        l = v
        s = k

print(s,"occurs",l,"times")