import random
import os 

chosen_number = random.randint(0,101)
print(chosen_number)

end_game = False

def start():
    print('''Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')
    difficulity()
    
def restart():
    global end_game
    restart = input("Do you want to play again ? yes/no: ").lower()
    if restart == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        start()
    elif restart == "no":
        print("Goodbye.")
        os.system('cls' if os.name == 'nt' else 'clear')
        end_game = True
        
def difficulity():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == 'easy':
        attempts(10)
    elif choice == 'hard':
        attempts(5)
    else:
        print("Please enter a valid difficulity. \n")
        difficulity()
        
def hints():
    global end_game
    guess = int(input("Make a guess: "))
    distance = abs(guess - chosen_number)
    
    if distance > 70:
        print("Extremely Far Off")
    elif distance > 60:
        if guess > chosen_number:
            print("Extremely High")
        else:
            print("Extremely Low")
    elif distance > 40:
        if guess > chosen_number:
            print("Way Too High")
        else:
            print("Way Too Low")
    elif distance > 30:
        if guess > chosen_number:
            print("Too High")
        else:
            print("Too Low")
    elif distance > 20:
        if guess > chosen_number:
            print("Slightly High")
        else:
            print("Slightly Low")
    elif distance > 10:
        if guess > chosen_number:
            print("A Bit High")
        else:
            print("A Bit Low")
    elif distance > 5:
        if guess > chosen_number:
            print("Very Close but High")
        else:
            print("Very Close but Low")
    elif guess > chosen_number:
            print("Very Close but Just High")
    elif guess < chosen_number:
            print("Very Close but Just Low")
    elif guess == chosen_number:
        print(f"Correct {guess} was the number you won!!!")
        restart()
        end_game = True
    
        
def attempts(attempt):
    global end_game
    while not end_game and attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        hints()
        if attempt == 0:
            print("You lost.")
            restart()
            end_game = True
        attempt -= 1
        attempts(attempt)
        
start()