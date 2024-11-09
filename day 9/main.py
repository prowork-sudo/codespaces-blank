import art


def highest_bidder(secreat_auction_bid):
    winner_name = ''
    winner_bid = 0
    for key in secreat_auction_bid:
        if secreat_auction_bid[key] > winner_bid:
            winner_bid = secreat_auction_bid[key]
            winner_name = key
    print(f"The winner is {winner_name} with the bid of {winner_bid}")


secreat_auction_bid = {}

running = True

while running:

    print(art.logo)

    print("welcome to  secteat auction program")

    name = input("What is your name? ")
    bid = int(input("What is your value? "))

    secreat_auction_bid[name] = bid

    cont = input("Are there any other bidders? 'yes' or 'no' \n")
    if cont == 'no':
        running = False
    print("\n" *200)


highest_bidder(secreat_auction_bid)