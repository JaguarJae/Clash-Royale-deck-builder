import cr_api

#user_tag = input("Clash Royale ID: ")
my_user_tag = "#QULPLURYG"
player_tag = my_user_tag
min_level = 15
max_level_diff = 16 - min_level

raw_top = cr_api.get_top()

player_cards = cr_api.get_user_cards(player_tag)

def check_deck_level(deck):
    for card in deck:
        card_name = card["name"]
        card_max_level = card["maxLevel"]
        user_card_level = int(player_cards[card_name]["level"])
        level_diff = card_max_level - user_card_level
        if level_diff <= max_level_diff:
            #print(card["name"], "level: valid")
            continue
        else:
            #print(card["name"], "level: non-valid")
            return False
    return True

def check_top_decks_level(top_decks):
    valid_decks = []
    for deck in top_decks:
        valid = check_deck_level(deck)
        if valid is True:
            valid_decks.append(deck)
    return valid_decks

def get_decks_card_list(decks):
    deck_number = 0
    clean_decks = {}
    for deck in decks:
        deck_number += 1
        clean_decks[deck_number] = []
        for card in deck:
            clean_decks[deck_number].append(card["name"])
    return clean_decks

top_decks = cr_api.get_top_decks()
leveled_decks = check_top_decks_level(top_decks)
clean_decks = get_decks_card_list(leveled_decks)

print(clean_decks)