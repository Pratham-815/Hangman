import random
import hangman_art

# Choosing word from the word list 
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Printing hangman logo
print(hangman_art.logo)

end_of_game = False
lives = 6

# Creating blanks 
display = []
for i in range(word_length):
    display += "_"


# Running the game
while not end_of_game:
    guess = input("Guess a letter : ").lower()

    # Checking if the guessed letter is repeated again
    if guess in display:
        print("You have already guessed that letter")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess   

    if guess not in chosen_word:
        print(f"You chose {guess}, that's not in the letter, you lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")
            print(f"The actual word was {chosen_word}")

    # Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("Hurray...You wons")

    print(hangman_art.stages[lives])

