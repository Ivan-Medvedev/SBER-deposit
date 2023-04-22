import json
import math

import pytest
import requests


def test_deposit():
    with open('test_1.json', 'r', encoding='utf-8') as file:
        test = json.load(file)
    response = requests.post(f'http://127.0.0.1:5000/deposit', json=test).json()
    assert math.isclose(response['31.03.2021'], 10150.75, abs_tol=0.01)


def test_deposit_failure():
    with open('test_2.json', 'r', encoding='utf-8') as file:
        test = json.load(file)
    response = requests.post(f'http://127.0.0.1:5000/deposit', json=test)
    assert response.status_code == 400
