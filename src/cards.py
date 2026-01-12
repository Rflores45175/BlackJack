class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.aces = 11

    def get_value(self):
        if self.rank in ('K', 'Q', 'J'):
            value = 10
        elif self.rank == 'A':
            value = 11
        else:
            value = int(self.rank)

        return value

    def is_ace(self):
        if self.rank == 'A':
            return True
        else:
            return False

    def card_name(self):
        card_name = self.suit + self.rank

        return card_name

    def __str__(self):
        return self.card_name()

    __repr__ = __str__