
list = [0,1,4,7,8,10,100]

a = 0
b = 0

def looking_for_pair(w):
    global a
    global b

    for i in list:
        if a != b and a + b == w:
            print(a)
            print(b)
            print("You won!")
            break

        elif i <= w:
            a = i

        for i in list:
            if i <= w:
                b = i


looking_for_pair(16)

