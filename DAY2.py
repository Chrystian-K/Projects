list = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

#nlist = []
#for v,i in enumerate(list):
i = list[0]
def func1():

    if list[i] == 99:
        print("koniec programu")
    else:
        z = list[1]
        x = list[2]
        a = list[z]
        b = list[x]
        list[i+3] = a + b
        list[i] = list[i+4]


def func2():
    print(list[i])
    if list[i] == 99:
        print("koniec programu")
    else:
        z = list[1]
        print(z)
        x = list[2]
        a = list[z]
        b = list[x]
        list[0] = a * b
        list[i] = list[i + 4]
        print(list[i])


func1()
func2()

#for i in list:
    #if i == 99:
        #print(list[0])
        #break
    #else:
        #func1()