import random
import os
from black_jack_art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_hit = random.choice(cards)
my_hit = random.choice(cards)

my_deck = []
dealers_deck = []
end_game = False


def shuffle():
    my_deck.clear()
    dealers_deck.clear()
    dealers_deck.append(dealer_hit)
    for _ in range(2):
        my_deck.append(random.choice(cards))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def stats():
    shuffle()
    print(f"Your cards: {my_deck}, current score: {sum(my_deck)}")
    print(f"Computers first card: {dealers_deck[0]}")

def hit_stats():
    print(f"Your cards: {my_deck}, current score: {sum(my_deck)}")
    print(f"Computers cards: {dealers_deck}, current score: {sum(dealers_deck)}")

def hit():
    global end_game
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if hit == "y":
        my_deck.append(random.choice(cards))
        if sum(my_deck) > 21:
            winner()
            return
        elif sum(my_deck) == 21:
            winner()
            return
        hit_stats()
    elif hit == "n":
        while sum(dealers_deck) < 17:
            dealers_deck.append(random.choice(cards))
        winner()
   
def winner():
    global end_game
    winner = None
    dealers_score = abs(sum(dealers_deck) - 21)
    my_score = abs(sum(my_deck) - 21)
    
    if my_score < dealers_score:
        winner = my_score
    elif dealers_score < my_score:
        winner = dealers_score
        
    if sum(my_deck) > 21:
        winner = dealers_score
        end_game = True
    elif sum(dealers_deck) > 21:
        winner = my_score
        end_game = True
    elif sum(my_deck) != 21 and sum(dealers_deck) == 21:
        winner = dealers_score
            
    if winner == my_score:
        end_game = True
        print(f"Your final hand: {my_deck}, final score: {sum(my_deck)}")
        print(f"Computer's final hand: {dealers_deck}, final score: {sum(dealers_deck)}")
        print("You Won!")
        start = input("Do you want to play again ? Type 'y' or 'n': ").lower()
        if start == "y":
            clear_screen()
            shuffle()
            begin()
        elif start == "n":
            print("Goodbye.")
            end_game = True
            
    elif winner == dealers_score:
        print(f"Your final hand: {my_deck}, final score: {sum(my_deck)}")
        print(f"Computer's final hand: {dealers_deck}, final score: {sum(dealers_deck)}")
        print("You Lost.")
        end_game = True
        start = input("Do you want to play again ? Type 'y' or 'n': ").lower()
        if start == "y":
            clear_screen()
            shuffle()
            begin()
        elif start == "n":
            print("Goodbye.")
            end_game = True
            
    else:
        print(f"Your final hand: {my_deck}, final score: {sum(my_deck)}")
        print(f"Computer's final hand: {dealers_deck}, final score: {sum(dealers_deck)}")
        print("Draw")
        end_game = True
        start = input("Do you want to play again ? Type 'y' or 'n': ").lower()
        if start == "y":
            clear_screen()
            shuffle()
            begin()
        elif start == "n":
            print("Goodbye.")
            end_game = True
            


def begin():
    global end_game
    end_game = False
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "n":
        print("Goodbye.")
        end_game = True
    elif start == "y":
        stats()
        while end_game == False:
            hit()
begin()