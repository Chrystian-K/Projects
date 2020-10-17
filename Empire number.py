# Emirp Number Valaidator

while True:

    x = int(input("Check if it is prime and emirp is prime: "))
    print(x)

    for i in range(2,x):
        if x % i == 0:
            print("Number provided is not prime")
            break
    else:
        x = int(str(x)[::-1])
        print(x)
        for i in range(2,x):
            if x % i == 0:
                print("Emirp number is not prime")
                break
        else:
            print('''
        CONGRATZ!!!
    
    ( )
    | | 
    | |______
    |  ______)
    |  ______)
    |  ______)
    |________)  
    ''')
