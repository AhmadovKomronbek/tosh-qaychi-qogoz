import random

end_of_game = False

while not end_of_game:
    while lives > 0 and "_" in display:
        guess = input("Guess a letter: ").lower()

        if guess in display:
            print(f"Sen allaqachon buni o'ylagansan yoki kiritgansan!")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosenword:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

        natija = ""
        for letter in display:
            natija += letter
        print(natija)
        print(stages[lives])

    if "" not in display:
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        end_of_game = False
    else:
        print("Thanks for playing!")
        end_of_game = True