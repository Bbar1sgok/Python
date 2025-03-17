import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
lives = 6

logo = hangman_art.logo
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_" for _ in range(word_length)]  # Create a clean placeholder
print("Word to guess: " + " ".join(display)) # Display the word with spaces for readability

game_over = False
guessed_letters = [] # Keep track of guessed letters (both correct and incorrect)
stages = hangman_art.stages

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print("Word to guess: " + " ".join(display))
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print("Word to guess: " + " ".join(display))

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
