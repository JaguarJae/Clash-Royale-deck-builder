import argparse
import json
import os

import api
import utils

my_tag = "#QULPLURYG"

parser = argparse.ArgumentParser(description="Clash Royale deck maker")

parser.add_argument("--level", "-l", required=True, type=int, help="Minimum card level")
parser.add_argument("--sync", "-s", help="Update locally saved decks", action="store_true")

tag_group = parser.add_mutually_exclusive_group(required=True)

tag_group.add_argument("--id", help="Your clash royale id")
tag_group.add_argument("--test", "-t", help="Use my tag as a test", action="store_true")

args = parser.parse_args()
if (args.test):
    user_tag = my_tag
else:
    user_tag = args.id.upper()

if (not user_tag.startswith('#')):
    user_tag = '#' + user_tag

min_level = args.level
player_cards = api.get_user_cards(user_tag)

if (args.sync or not os.path.exists("cache.json")):
    print("Fetching API info")
    raw_top_decks = api.get_top_decks()
    top_decks = utils.fetch_card_names(raw_top_decks)

    if top_decks is not None:
        with open("cache.json", "w", encoding="utf-8") as file:
            json.dump(top_decks, file, indent=4, ensure_ascii=False)
    else:
        print("Not updated cache because there is no info")
else:
    with open("cache.json", "r", encoding="utf-8") as file:
        top_decks = json.load(file)


if __name__ == "__main__":
    leveled_decks = utils.check_top_decks_level(top_decks, player_cards, min_level)
    card_decks = utils.get_decks_card_list(leveled_decks)

    if not card_decks:
        print("No deck fits the minimum level")
    else:
        for num, cards in card_decks.items():
            print(f"\n{num}: ", end="")
            for card in cards:
                print(f"{card} - ", end="")
        print("\n")
