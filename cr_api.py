import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
token = os.getenv("TOKEN")

base_url = "https://api.clashroyale.com/v1"
headers = {
    "Authorization" : f"Bearer {token}"
}

session = requests.Session()
session.headers = headers

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
        top_decks = list(executor.map(fetch_deck, top))
    
    return top_decks

