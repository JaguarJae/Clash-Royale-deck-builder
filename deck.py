from card import Card


class Deck:
    def __init__(self, player, rank, cards : list[Card]):
        self.player = player
        self.rank = rank
        self.cards = cards

        if len(cards) != 8:
            raise ValueError("Deck must have 8 cards")

    def min_level(self):
        level_thresold = 16
        for card in self.cards:
            level_thresold = min(level_thresold, card.level)

        return level_thresold
