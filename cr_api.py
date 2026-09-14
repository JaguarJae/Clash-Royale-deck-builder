import os
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

base_url = "https://api.clashroyale.com/v1"
headers = {
    "Authorization" : f"Bearer {token}"
}

session = requests.Session()
session.headers.update(headers)

def get_user_info(raw_user_tag):
    user_tag = quote(raw_user_tag)
    url = f"{base_url}/players/{user_tag}"
    response = session.get(url, headers=headers)
    return response.json()

def get_top():
    url = f"{base_url}/locations/global/pathoflegend/players"
    response = requests.get(url=url, headers=headers)
    return response.json()["items"]

def get_user_cards(user_tag):
    user_info = get_user_info(user_tag)
    user_cards = {c["name"]: c for c in user_info["cards"]}
    return user_cards

def get_top_decks():
    top = get_top()
    def fetch_deck(player):
        player_info = get_user_info(player["tag"])

        return player_info["currentDeck"]

    with ThreadPoolExecutor(max_workers=15) as executor:
        results = list(executor.map(fetch_deck, top))

    top_decks = [deck for deck in results if deck]

    return top_decks
