def generate_even_numbers():
    x = 1
    yield x*x
    if x == 1:
        x +=1
    

generate_even_numbers()