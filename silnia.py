import time


s = int(input("podaj liczbe dla ktorej chcesz wyliczyc silnie: "))

def suma1(s):
    x = 0
    for i in range(s+1):
        x = x+i
    return x

def suma2(s):
    return(sum([i for i in range(1,s+1)]))

def suma3(s):
    return (1 + s) / 2 * s

def timer(start):
    end = time.perf_counter()
    return start - end


def function_performance(func, arg, how_many_times = 1):
    x = 0
    
    for i in range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        x = x+(end-start)
    return x

'''
start = time.perf_counter()
print(suma1(s))
print(timer(start))

start = time.perf_counter()
print(suma2(s))
print(timer(start))

start = time.perf_counter()
print(suma3(s))
print(timer(start))
'''

print(function_performance(suma1, s,1231))
print(function_performance(suma2, s,123))
print(function_performance(suma3, s,43534))
