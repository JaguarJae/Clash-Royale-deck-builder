from dotenv import load_dotenv
import os
import requests

load_dotenv()
#user_tag = input("Clash Royale ID: ")
my_user_tag = "%23QULPLURYG"
user_tag = my_user_tag
token = os.getenv("TOKEN")

base_url = "https://api.clashroyale.com/v1"

headers = {
    "Authorization" : f"Bearer {token}"
}

def get_user_info(user_tag):
    url = f"{base_url}/players/{user_tag}"
    response = requests.get(url, headers=headers)
    return response.json()

user_info = get_user_info(user_tag)

print (user_info["cards"])