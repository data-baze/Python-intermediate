import requests

req = requests.get("#")
person = req.json()
# print(person) #prints the entire json 
print(f"Name is \t\t\t{person['name']}")#prints only name in the json
print(f"Birth year is \t\t\t{person['birth_year']}")#prints only birthyear in the json

print("Films involved in:")
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print("Film is:", film['title'])
