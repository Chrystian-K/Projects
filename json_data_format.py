
'''json.dump(data, nameOfFileHandler, ensure_ascii=False) -
                               zapisuje dane do pliku w postacji json'''


import json

film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

encodedFilm = json.dumps(film, ensure_ascii=False)

with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)
"""
{  
   "title":"Ale ja nie będę tego robił!",
   "release_year":1969,
   "won_oscar":true,
   "actors":[  
      "Arkadiusz Włodarczyk",
      "Wiolleta Włodarczyk"
   ],
   "budget":null,
   "credits":{  
      "director":"Arkadiusz Włodarczyk",
      "writer":"Alan Burger",
      "animator":"Anime Animatrix"
   }
}
"""

#print(json.dumps(film))
print(json.dumps(film, ensure_ascii=False,indent=4,sort_keys=True))

with open("sample.json", "w", encoding="UTF-8") as file:
   plik = json.dump(film, file, ensure_ascii=False,indent=4,sort_keys=True)

#plik = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

odkodowanyPlik = json.loads(plik, encoding="UTF-8")

print(odkodowanyPlik)
import pprint
with open("sample.json", encoding="UTF-8") as file:
   wynik = json.load(file)

pprint.pprint(odkodowanyPlik)