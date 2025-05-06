import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd6cbd359fd8fe0afe0355a5eaf98a444'
HEADER = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}

body_registration = {"trainer_token" : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}


body_pathc_create = {
    "pokemon_id": "309568",
    "name": "Паровозик Томас"
}

body_catch = {
    "pokemon_id": "309567"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)


response_patch_create = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_pathc_create)

print(response_patch_create.text)



response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)

print(response_catch.text)