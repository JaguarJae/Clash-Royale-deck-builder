def fetch_card_names(raw_decks):
    decks = []
    for raw_deck in raw_decks:
        deck = []
        for card in raw_deck:
            deck.append(card["name"])
        if (len(deck) != 8):
            print("Something happened with this deck", deck)
        for array_deck in decks:
            if (deck != array_deck):
                decks.append(deck)
    return decks

def check_deck_level(deck, player_cards, min_level):
    for card in deck:
        if card not in player_cards:
            return False

        card_info = player_cards[card]
        card_max_level = card_info["maxLevel"]
        user_raw_card_level = int(card_info["level"])

        user_card_level = 16 - card_max_level + user_raw_card_level
        if (user_card_level < min_level):
            return False
    return True

def check_top_decks_level(top_decks, player_cards, level):
    valid_decks = []
    for deck in top_decks:
        valid = check_deck_level(deck, player_cards, level)
        if valid is True:
            valid_decks.append(deck)
    return valid_decks

def get_decks_card_list(decks):
    clean_decks = {}

    for i, deck in enumerate(decks, start=1):
        clean_decks[i] = []

        for card in deck:
            clean_decks[i].append(card)

    return clean_decks
