import cr_api

#user_tag = input("Clash Royale ID: ")
my_user_tag = "#QULPLURYG"
player_tag = my_user_tag
min_level = 15
max_level_diff = 16 - min_level

raw_top = cr_api.get_top()

player_cards = cr_api.get_user_cards(player_tag)

def check_deck_level(deck):
    valid = True
    for card in deck:
        card_name = card["name"]
        card_max_level = card["maxLevel"]
        user_card_level = int(player_cards[card_name]["level"])
        level_diff = card_max_level - user_card_level
        if level_diff <= max_level_diff:
            print(card["name"], "level: valid")
            continue
        else:
            print(card["name"], "level: non-valid")
            valid = False
    return valid

top_1_deck = cr_api.get_top_decks()[0]

print(check_deck_level(top_1_deck))