listSample = [1,4,512,24]

listSample2 = listSample

listSample2.append(465)


a = 4

b = a


b = 7



c = 5
print(id(c))

def add(c, amount = 1):
    print(id(c))
    c = c+amount
    print(id(c))

add(c)


