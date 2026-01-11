import random

class Deck:
    def __init__(self, list_cards):
        self.deck = list_cards.copy()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop()
        return card

    def cards_in_deck(self):
        return len(self.deck)

    def display_deck(self):
        card_list = ""
        for card in self.deck:
            card_list = card_list + str(card) + ", "

        return card_list.rstrip(", ")

    def is_valid_deck(self):
        if 0 < self.cards_in_deck() <= 52:
            return True
        else:
            return False

    def __str__(self):
        remaining_cards = self.cards_in_deck()
        return "Remaining Cards: " + str(remaining_cards)
