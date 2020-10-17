# Program is counting a number of coins and bills that needs to be given as a change
#import pdb
import zakupy

change = zakupy.b
a = 0
coins = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000)

#pdb.set_trace()
def magic():
    global change
    global a
    #pdb.set_trace()
    for i in coins:

        if round(i, 2) <= round(change, 2):
            a = i
        elif round(change, 2) == 0:
            break
        else:
            round(a, 2)
            change = change - a
            if a < 10:
                print("Change coins has value of " + str(a))
            else:
                print("Change bill has value of " + str(a))
            a = 0
            if True:
                magic()

magic()