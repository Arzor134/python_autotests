import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
PATH = '/trainers'
HEADAR = {'trainer_id': '284', 'Content-Type': 'application/json', 'trainer_token': 'ee7a8a9b6a260971801039e35444ec91'}

#def test_get_trainers():
    # KTI-1. GET trainers ответ с кодом 200

    #response = requests.get(url=f'{URL}{PATH}', headers=HEADAR, timeout=5)
    #assert response.status_code == 200, 'unexpected status_coded'

def test_get_trainers():
    # KTI-2. GET trainers ответ именем тренира

    response = requests.get(url=f'{URL}{PATH}', headers=HEADAR, timeout=5)
    #assert response.status_code == 200, 'unexpected status_coded'
    # Добавляем проверку на наличие имени тренера в ответе
    assert 'Roman' in response.text, 'Имя тренера найдено в ответе'
