import argparse
import json
import os

import cr_api

my_tag = "#QULPLURYG"

parser = argparse.ArgumentParser(description="Clash Royale deck maker")

parser.add_argument("--level", "-l", required=True, type=int, help="Minimum card level")
parser.add_argument("--sync", "-s", help="Update locally saved decks", action="store_true")

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("--id", help="Your clash royale id")
group.add_argument("--test", "-t", help="Use my tag as a test", action="store_true")

args = parser.parse_args()
if (args.test):
    user_tag = my_tag
else:
    user_tag = args.id.upper()

if (not user_tag.startswith('#')):
    user_tag = '#' + user_tag

min_level = args.level

player_cards = cr_api.get_user_cards(user_tag)

if (args.sync or not os.path.exists("cache.json")):
    top_decks = cr_api.get_top_decks()
    if top_decks is not None:
        with open("cache.json", "w", encoding="utf-8") as file:
            json.dump(top_decks, file, indent=4, ensure_ascii=False)
    else:
        print("Not updated cache because there is no info")

with open("cache.json", "r", encoding="utf-8") as file:
    top_decks = json.load(file)

def check_deck_level(deck, player_cards):
    for card in deck:
        if card["name"] not in player_cards:
            return False

        card_max_level = card["maxLevel"]
        user_card_level = int(player_cards[card["name"]]["level"])

        level_diff = card_max_level - user_card_level
        max_level_diff = 16 - min_level

        if level_diff <= max_level_diff:
            continue
        else:
            return False
    return True

def check_top_decks_level(top_decks):
    valid_decks = []
    for deck in top_decks:
        valid = check_deck_level(deck, player_cards)
        if valid is True:
            valid_decks.append(deck)
    return valid_decks

def get_decks_card_list(decks):
    clean_decks = {}

    for i, deck in enumerate(decks, start=1):
        clean_decks[i] = []

        for card in deck:
            clean_decks[i].append(card["name"])

    return clean_decks


if __name__ == "__main__":
    leveled_decks = check_top_decks_level(top_decks)
    card_decks = get_decks_card_list(leveled_decks)

    for num, cards in card_decks.items():
        print(f"\n{num}: ")
        for card in cards:
            print(f"{card} ")
