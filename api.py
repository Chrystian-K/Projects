import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

print(datetime.today())
roznicaCzasu = timedelta(days=7)
dataNasza = datetime.today() - roznicaCzasu
print(dataNasza)
'''
params = {"site" : "stackoverflow",
          "sort": "votes",
          "order" : "desc",
          "fromdate" : int(dataNasza.timestamp()),
          "tagged" : "python",
          "min" : 10
          }

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Nie działa to scierwo")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
'''
params = {
    "amount" : 2

}

c = requests.get("https://cat-facts.herokuapp.com/facts/random", params)


try:
    questions = c.json()
    print(c)
except json.decoder.JSONDecodeError:
    print("Nie działa to scierwo")
else:
    for cat in questions:
        print(cat["text"])