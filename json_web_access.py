import requests
import json


wynik = requests.get("http://jsonplaceholder.typicode.com/todos")

def liczenie_ilosc_zadan(zadania):
    skonczoneZdaniaPrzezLudzi = dict()
    for entry in zadania:
        if entry["completed"] == True:
            try:
                skonczoneZdaniaPrzezLudzi[entry["userId"]] += 1
            except KeyError:
                skonczoneZdaniaPrzezLudzi[entry["userId"]] = 1
    return skonczoneZdaniaPrzezLudzi

def osoby_co_najwiecej_zrobily(skonczoneZdaniaPrzezLudzi):
    osobyCoNajwieciejzrobily = []
    maxWykonanychZadan = max(skonczoneZdaniaPrzezLudzi.values())
    for userId, ukonczoneZadania in skonczoneZdaniaPrzezLudzi.items():
        if ukonczoneZadania == maxWykonanychZadan:
            osobyCoNajwieciejzrobily.append(userId)
            
    return osobyCoNajwieciejzrobily


def get_keys_with_top_values(my_dict):
    return [
        key
        for (key,value) in my_dict.items()
        if value == max(my_dict.values())
        ]


try:
    zadania = wynik.json()
except json.decoder.JSONDecodeError:
    print("Nie ma takiej strony")
else:
    skonczoneZdaniaPrzezLudzi = liczenie_ilosc_zadan(zadania)
    topPracowicy = osoby_co_najwiecej_zrobily(skonczoneZdaniaPrzezLudzi)


print(topPracowicy)

#sposob 1 na wyciagniecie danych o uzytkownikiu
wynik = requests.get("http://jsonplaceholder.typicode.com/users")

uzytkownicy = wynik.json()
for uzytkownik in uzytkownicy:
    if uzytkownik["id"] in topPracowicy:
        print("ciasteczko idzie dla:", uzytkownik["name"])


#sposob 2 na wyciagniecie danych o uzytkownikiu

wynik = requests.get("http://jsonplaceholder.typicode.com/users")
uzytkownicy = wynik.json()

#sposob 3

def zmiana_wyniku_w_parametr(topPracowicy, key="id"):
    laczenie = key + "="

    ostatniPrzebiegPetli = len(topPracowicy)
    i = 0
    for item in topPracowicy:
        i += 1
        if i == topPracowicy:
            laczenie += str(item)
        else:
            laczenie += str(item) + "&" + key + "="

    return laczenie

laczenie = zmiana_wyniku_w_parametr(topPracowicy)
laczenie = zmiana_wyniku_w_parametr([1,5,7,8,9])

wynik = requests.get("http://jsonplaceholder.typicode.com/users", params=laczenie)
uzytkownicy = wynik.json()

for uzytkownik in uzytkownicy:
    print("ciasteczko idzie dla:", uzytkownik['name'])