#
# test api
#

import requests

URL = 'https://api.pokemonbattle.me/v2'
PATH = '/pokemons'

HEADAR = {'Content-Type': 'application/json', 'trainer_token': 'ee7a8a9b6a260971801039e35444ec91'}

body = {
    "name": "PsyDuck",
    "photo": "https://dolnikov.ru/pokemons/albums/054.png"
    }

response = requests.post(url=f'{URL}{PATH}', json=body, headers=HEADAR, timeout=5)
print(f'статус код: {response.status_code}. Сообщение: {response.json()["message"]}')
