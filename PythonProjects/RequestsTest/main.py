import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0deba459599acd8f6b689af48df8ce7c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "psvqa2025@gmail.com",
    "password": "!8fVwu9CLbZAGuV"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "dino1",
    "photo_id": 333
}

body_rename = {
    "pokemon_id": "282288",
    "name": "dino2",
    "photo_id": 333
}

body_pokeball = {
    "pokemon_id": "282288"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''