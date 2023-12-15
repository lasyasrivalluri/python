import random
list = ["apple", "banana", "mango", "orange", "grapes"]
def hangman():
    word = random.choice(list)
    guessed_letters = []
    tries = 6
    while tries > 0:
        display_word = "".join(letter if letter in guessed_letters else '_' for letter in word)
        print("Current word:", display_word)

        x = input("Enter a letter: ").lower()

        if x in guessed_letters:
            print("You already guessed that letter!")
        elif x in word:
            print("Correct!")
            guessed_letters.append(x)
        else:
            print("Wrong!")
            tries -= 1
            print("Tries remaining:", tries)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the correct word:"+word)
            break

        

        if tries == 0:
            print("Sorry, game over The correct word was:"+word)

hangman()