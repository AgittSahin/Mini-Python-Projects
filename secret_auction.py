from auction_art import logo
import os

print(logo)

bidders = {}

def ask_bidder():
    name = input("What is your name: ")
    price = int(input("What is your offer: "))
    new_bidder = input("Are there any other bidder ?  yes/no: ").lower()
    bidders[name] = price
    if new_bidder == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        ask_bidder()
    elif new_bidder == "no":
        return
    else:
        print("Please enter a valid answer.")
        os.system('cls' if os.name == 'nt' else 'clear')
        ask_bidder()
        
def highest_bidder():
    highest_bid = 0
    winner = ""
    for bidder, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The highest bidder is {winner} with a bid of ${highest_bid}.")

ask_bidder()
highest_bidder()