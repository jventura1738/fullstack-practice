# Justin Ventura
from flask import Blueprint, request, render_template

import requests
from requests.auth import HTTPBasicAuth

import random

# Importing this in __init__
views = Blueprint('views', __name__)


# Home page route:
@views.route('/')
def home():
    """Home page view route.

    This function runs whenever the home page (url below) is requested.
        ex) -> localhost:5000/

    Returns the home page:
    """
    return '<h1>Home page</h1>'


# Get a random pokemon image url.
@views.route('/get-random-pokemon', methods=['GET'])
def get_random_pokemon():
    url = f'https://pokeapi.co/api/v2/pokemon/{random.randint(1, 152)}'
    pokemon = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
    color = 'front_shiny' if random.randint(0, 30) == 15 else 'front_default'
    return pokemon.json()['sprites'][color]
