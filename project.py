import requests

Pokename = input("What's your fav Pokemon?")
url = f"https://Pokemon.io/{Pokename}"

req = requests.get(url)
Pokemon = req.json()
print(Pokemon)
