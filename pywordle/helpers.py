from termcolor import colored

def check_letters(player_guess, word):
    position_map = {i: None for i in range(5)}
    for i in range(len(player_guess.word)):
        if player_guess.word[i] == word.random_word[i]:
            position_map[i] = "green"
            player_guess.correct_letters()
        elif player_guess.word[i] in word.random_word:
            position_map[i] = "yellow"
    
    return position_map

def print_answer(position_map, player_guess):
    for i in position_map:
        if not position_map[i]:
            print(colored(player_guess.word[i], "red"), end="")
        elif position_map[i] == "green":
            print(colored(player_guess.word[i], "green"), end="")
        else:
            print(colored(player_guess.word[i], "yellow"), end="")