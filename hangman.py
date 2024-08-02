import hangman_words
import random
import hangman_art
import os

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed_letters = []

print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(f"Guessed Letters: {guessed_letters}")
    
    if len(guess) != 1:
        print("Please enter a single letter.")
    else:
        if guess in guessed_letters:
            print(f"You have already guessed this letter before letter: {guess}")
        else:
            guessed_letters.append(guess)
            
            if guess in chosen_word:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter
            else:
                print(f"Sorry wrong guess {guess} is not in the word.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])