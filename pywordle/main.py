from word import Word
from player import Player
from guess import Guess
from PyDictionary import PyDictionary
from termcolor import colored

dictionary = PyDictionary()

def main():
    print("Welcome to PyWordle")
    print("⬜️ ⬜️ ⬜️ ⬜️ ⬜️")

    word = Word()
    player = Player()
    guess = Guess(Player)

    guesses = []

    while player.ATTEMPTS < guess.MAX_ATTEMPTS:
        print("")
        player_guess = Guess.get_guess()

        if not player_guess.validate():
            print("Enter a valid word with 5 letters")
        elif player_guess.guess in guesses:
            print("You already guessed this word")
        else:
            player.lost_attempt()
            guesses.append(player_guess.guess)
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

def check_letters(player_guess, word):
    position_map = {i: None for i in range(5)}
    for i in range(len(player_guess.guess)):
        if player_guess.guess[i] == word.random_word[i]:
            position_map[i] = "green"
            player_guess.correct_letters()
        elif player_guess.guess[i] in word.random_word:
            position_map[i] = "yellow"
    
    return position_map

def print_answer(position_map, player_guess):
    for i in position_map:
        if not position_map[i]:
            print(player_guess.guess[i], end="")
        elif position_map[i] == "green":
            print(colored(player_guess.guess[i], "green"), end="")
        else:
            print(colored(player_guess.guess[i], "yellow"), end="")

if __name__ == "__main__":
    main()