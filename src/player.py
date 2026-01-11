
class Player:
    def __init__(self, funds):
        self.hand = []
        self.funds = funds
        self.bet = 0

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def place_bet(self, amount):
        self.bet = amount

    def win_bet(self, win_amount):
        self.funds += win_amount

    def lose_bet(self, lose_amount):
        self.funds -= lose_amount

    def new_game(self):
        self.hand = []
        self.bet = 0

    def hand_total(self):
        total = 0
        aces = 0

        for card in self.hand:
            if card.is_ace():
                aces += 1

            total += card.get_value()

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def show_hand(self):
        for card in self.hand:
            print(card)

    def is_busted(self):
        return self.hand_total() > 21

    def has_blackjack(self):
        pass

    def can_double_down(self):
        pass

    def can_split(self):
        pass

    def can_insurance(self):
        pass
