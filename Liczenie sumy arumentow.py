a = 0

while True:
    b = input("""
    Jakie liczby chcesz dodac?: 
    Wpisz zakoncz, zeby przestac dodawac i wypisac sume
    """)
    if b == "zakoncz":
        print(a)
        break
    else:
        b = int(b)
        print(b)
        a = a+b

def count(*arg):
    return sum(arg)

print(count(a))