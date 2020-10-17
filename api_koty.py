import requests
import json
import webbrowser
import credentials

from pprint import pprint


r = requests.get("https://api.thecatapi.com/v1/favourites/", headers = credentails.header)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("zły format", r.text)
else:
    print(content)