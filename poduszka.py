import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

print(datetime.today())
roznicaCzasu = timedelta(days=7)
dataNasza = datetime.today() - roznicaCzasu
print(dataNasza)

client_id : "07e406aa9455432bb29806aceb0ebea0"
'''
params = {"string": "poduszki ciążowe",
        "bmatch" : "baseline-product-cl-eyesa2-engag-dict45-uni-1-4-0903",
        "price_to": 220,
        "prince_from": 90
          }
'''
params = {"response_type": "code",
        "client_id" : "07e406aa9455432bb29806aceb0ebea0",
        "redirect_uri": "https://allegro.pl",
        }
client_id = "07e406aa9455432bb29806aceb0ebea0"
Content_Typ=  "application/vnd.allegro.public.v1+json"
Accept= "application/vnd.allegro.public.v1+json"

#r = requests.get("https://allegro.pl/auth/oauth/authorize?response_type=code&client_id=07e406aa9455432bb29806aceb0ebea0&redirect_urihttps://allegro.pl", params)
r = requests.get("https://api.allegro.pl/auth/oauth/authorize", client_id,)

poduszki = r.json()
print(poduszki)

try:
    poduszki = r.json()
except json.decoder.JSONDecodeError:
    print("Nie działa to scierwo")
else:
    for poduszka in poduszki:
        print(poduszki)
        #webbrowser.open_new_tab(poduszka)




