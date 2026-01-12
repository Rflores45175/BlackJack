from player import Player
from deck import Deck
from cards import Card


def create_cards():
    VALID_SUIT = ["C", "D", "H", "S"]
    VALID_RANK = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    card_list = []
    for suit in VALID_SUIT:
        for rank in VALID_RANK:
            card_list.append(Card(suit, rank))

    return card_list

def create_deck(card_list):
    deck = Deck(card_list)

    return deck


def print_stats(deck :Deck, cards, player:Player, dealer:Player):
    print(deck)
    print(cards)
    print(player)
    print(dealer)

def place_bet(player: Player):
    while True:
        try:
            bet = int(input("Enter the amount you want to bet: "))

            if bet <= 0:
                print("Invalid amount. Please try again.")
                continue

            if bet > player.funds:
                print("You do not have enough funds. Please enter a valid amount.")
                continue

            player.place_bet(bet)
            break

        except ValueError:
            print("Please enter a numeric value.")
            continue

def show_table_cards(player_list, show_hole_card = False):

    print(f"==============================================================")
    for player in player_list:
        if player.player_name == "Dealer" and show_hole_card == False:
            #TODO fix dealer hand total. not sure how to do that yet proabably just make a fucniton in the player class.
            print(f"{player.player_name} your hand is: {player.hand[0]}. Hand Total: {player.hand[0].get_value()}")
        else:
            print(f"{player.player_name} your hand is: {player.hand}. Hand Total: {player.hand_total()}")
    print(f"==============================================================")



def main():
    print("=============WELCOME TO BLACKJACK=============")

    #create objects. Need a card objects, deck object, player objects.
    cards = create_cards()
    deck = create_deck(cards)
    dealer = Player(player_name="Dealer", funds=1000)

    # Ask player for name
    player_name = input("What is your name? ")
    player1 = Player(player_name=player_name, funds=1000)

    player_list = [player1, dealer]

    while True:
        print("MAIN GAME LOOP ENTERED!") # TODO DELETE LATER USED FOR DEBUGGING

        if player1.funds <= 0:
            print("GAME OVER! \nNO FUNDS REMAINING")
            break

        print("====================BETS====================")
        place_bet(player1)

        print(f"====================CARDS ARE BEING DEALT!====================")
        # Cards are passed to each player one at a time.
        for i in range(2):
            for player in player_list:
                delt_card = deck.deal_card()
                player.add_card_to_hand(delt_card)

                print(f"Player: {player.player_name}, Was delt card: {delt_card}")

        show_table_cards(player_list, False)

        print("====================MAKE A SELECTION!====================")
        print("1. Hit")
        print("2. Stand")
        print("3. Surrender")
        player_action = int(input("Enter your choice: "))





        break

if __name__ == '__main__':
    main()

