from wonderwords import RandomWord
from PyDictionary import PyDictionary
from termcolor import colored

r = RandomWord()
dictionary = PyDictionary()

def main():
    word = r.word(word_min_length=5, word_max_length=5)

    print("Welcome to PyWordle!")
    print("⬜️ ⬜️ ⬜️ ⬜️ ⬜️")

    get_guess(word)

def get_guess(word):
    attempts = 0
    attempts_list = []
    MAX_ATTEMPTS = 6
    MAX_LETTERS = 5

    while attempts < MAX_ATTEMPTS:
        print("")
        guess = input("Guess word: ").lower().strip()
        valid_guess = validate_guess(guess, MAX_LETTERS)
        green_letters = 0

        if guess in attempts_list:
            print("You already guessed this word")
        elif valid_guess:
            attempts += 1
            attempts_list.append(guess)
            position_dict, green_letters = check_letters_color(guess, word)
            print_answer(position_dict, guess)
            print(get_remaining_attempts(attempts, MAX_ATTEMPTS))
        else:
            print("Enter a valid word with 5 letters")

        if green_letters == MAX_LETTERS:
            print("")
            print("Congratulations! You found out the word :)")
            break

    if attempts == MAX_ATTEMPTS and green_letters < MAX_LETTERS:
        print("")
        print(f"You lost! The word was {word} :(")

def validate_guess(guess, MAX_LETTERS):
    if dictionary.meaning(guess, disable_errors=True) and len(guess) == MAX_LETTERS:
        return True
    else:
        return False

def check_letters_color(guess, word):
    position_dict = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None
    }
    green_letters = 0

    # compare each letter of the guessed word with the random word
    for i in range(len(guess)):
        if guess[i] in word and guess[i] == word[i]:
            position_dict[i+1] = "green"
            green_letters += 1
        elif guess[i] in word and guess[i] != word[i]:
            position_dict[i+1] = "yellow"
    return position_dict, green_letters

def print_answer(position_dict, guess):
    for i in position_dict:
        if not position_dict[i]:
            print(guess[i-1], end="")
        elif position_dict[i] == "green":
            print(colored(guess[i-1], "green"), end="")
        else:
            print(colored(guess[i-1], "yellow"), end="")

    print("")

def get_remaining_attempts(attempts, MAX_ATTEMPTS):
    return f"You have {MAX_ATTEMPTS - attempts} attempts left"

if __name__ == "__main__":
    main()