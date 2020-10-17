import random
from collections import Counter

'''x = 0
while x<100:
    x = x+1
    print(random.uniform(0,100))

def hit_chance(per):
    default_value = random.uniform(0,100)
    if default_value < per:
        return "hit"
    else:
        return "miss"

print(hit_chance(50))


x = 0

listHit = []
while x < 100:
    x = x+1
    listHit.append(hit_chance(50))

print(listHit.count("hit"))
from collections import Counter
dictListHit = Counter(listHit)

print(dictListHit)'''

movieList = ["tytul 1","tytul 2","tytul 3","tytul 4"]
events = ["śmierć", "wygrana", "przegrana", "utrata zlota", "utrata zycia"]
nagrodaZeSkrzynki = ["zielona","pomaraczona","purpurowa","legendarna"]

print(random.choice(movieList))
print(Counter(random.choices(nagrodaZeSkrzynki, [80,15,4,1],k = 100)))