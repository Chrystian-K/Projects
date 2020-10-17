import time

def Function_Performance(func, arg, how_many_times = 1):
    x = 0

    for i in range (0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        x = x+ (end - start)

    return x

setCon = {i for i in range(1000)}
listCon = [i for i in range(1000)]

liczba_szukana = int(input("jakiej liczby szukasz?: "))

def czy_jest_w_liscie(funkcja):
    
    if liczba_szukana in funkcja:
        return True
    else:
        return False

print(czy_jest_w_liscie(setCon))
print(czy_jest_w_liscie(listCon))

print(Function_Performance(czy_jest_w_liscie, setCon, how_many_times = 123170))
print(Function_Performance(czy_jest_w_liscie, listCon, how_many_times = 123170))
