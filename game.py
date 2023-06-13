from pywordle.word import Word
from pywordle.player import Player
from pywordle.guess import Guess
from pywordle.helpers import check_letters, print_answer

def main():
    print("Welcome to PyWordle")
    print("⬜️ ⬜️ ⬜️ ⬜️ ⬜️")

    word = Word()
    player = Player()
    guess = Guess()

    guesses = []

    while player.ATTEMPTS < guess.MAX_ATTEMPTS:
        print("")
        player_guess = Guess.get_guess()

        if not player_guess.validate():
            print("Enter a valid word with 5 letters")
        elif player_guess.word in guesses:
            print("You already guessed this word")
        else:
            player.lost_attempt()
            guesses.append(player_guess.word)
            position_map = check_letters(player_guess, word)
            print_answer(position_map, player_guess)

        print("")
        print(f"Remaining attempts: {guess.MAX_ATTEMPTS - player.ATTEMPTS}")

        if player_guess.GREEN_LETTERS == word.length:
            print("")
            print("Congratulations! You found out the word :)")
            break

    if player.ATTEMPTS == guess.MAX_ATTEMPTS and player_guess.GREEN_LETTERS < word.length:
        print("")
        print(f"You lost! The word was {word.random_word} :(")

if __name__ == "__main__":
    main()