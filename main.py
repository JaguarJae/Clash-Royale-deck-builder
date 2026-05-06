import cr_api

user_tag = input("Clash Royale tag (include #):")
min_level = int(input("Minimum card level:"))
#my_tag = "#QULPLURYG"
player_cards = cr_api.get_user_cards(user_tag)

def check_deck_level(deck, min_level, player_cards):
    for card in deck:
        card_name = card["name"]

        card_max_level = card["maxLevel"]
        user_card_level = int(player_cards[card_name]["level"])

        level_diff = card_max_level - user_card_level
        max_level_diff = 16 - min_level

        if level_diff <= max_level_diff:
            continue
        else:
            return False
    return True

def check_top_decks_level(top_decks, min_level):
    valid_decks = []
    for deck in top_decks:
        valid = check_deck_level(deck, min_level, player_cards)
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

def get_user_valid_decks(min_level):
    top_decks = cr_api.get_top_decks()
    leveled_decks = check_top_decks_level(top_decks, min_level)
    card_decks = get_decks_card_list(leveled_decks)
    return card_decks

clean_decks = get_user_valid_decks(min_level)
print(clean_decks)