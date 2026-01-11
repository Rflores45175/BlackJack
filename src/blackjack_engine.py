from player import Player
from deck import Deck
from cards import Card


def create_cards():
    VALID_SUIT = {"C", "D", "H", "S"}
    VALID_RANK = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}

    card_list = []
    for suit in VALID_SUIT:
        for rank in VALID_RANK:
            card_list.append(Card(suit, rank))

    return card_list

def create_deck(card_list):
    deck = Deck(card_list)

    return deck

def main():
    cards = create_cards()
    deck1 = create_deck(cards)

