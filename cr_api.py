import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote

load_dotenv()

token = os.getenv("TOKEN")

base_url = "https://api.clashroyale.com/v1"
headers = {
    "Authorization" : f"Bearer {token}"
}

def get_user_info(raw_user_tag):
    user_tag = quote(raw_user_tag)
    url = f"{base_url}/players/{user_tag}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_top():
    url = f"{base_url}/locations/global/pathoflegend/players?limit=50"
    response = requests.get(url=url, headers=headers)
    return response.json()["items"]

def get_user_cards(user_tag):
    user_info = get_user_info(user_tag)
    user_cards = {c["name"]: c for c in user_info["cards"]}
    return user_cards

def get_top_decks():
    top = get_top()
    top_decks = []
    for player in top:
        player_info = get_user_info(player["tag"])
        player_deck = player_info["currentDeck"]
        top_decks.append(player_deck)
    return top_decks

