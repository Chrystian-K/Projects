import json

film = {
"dupa" : 123,
"mleko" : 84,
"z" : (5+6)*7,
"wynik": "to chyba jakas pomylka"

}

print(json.dumps(film))