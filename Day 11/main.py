import art
import random

player_card = []
dealer_card = []


def draw_cards():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_deck)
    return card

def sum(arra):
    s = 0
    for i in arra:
        s += i
    return s


def start():
    player_card = [draw_cards(), draw_cards()]
    dealer_card = [draw_cards(), draw_cards()]
    sum_print(player_card, dealer_card)
    return player_card, dealer_card

def sum_print(player_card, dealer_card):
    print(f"Your cards:{player_card} current score is {sum(player_card)}")
    print(f"Computers first card is: {dealer_card[0]}")

def cont():
    cont = input("Type 'y' to get another card, type 'n' to pass: ")
    if cont == "y":
        player_card.append(draw_cards())
        print((player_card, dealer_card))

        sum_print(player_card, dealer_card)

    else:
        dealer_card.append(draw_cards())
        sum_print(player_card, dealer_card)


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y":

    print(art.logo)

    start()
    print((player_card, dealer_card))

    cont()

    
    

