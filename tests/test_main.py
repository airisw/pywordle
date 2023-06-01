import pytest
from pywordle.main import check_letters
from pywordle.word import Word
from pywordle.guess import Guess

def test_check_letters_green():
    word = Word()
    word.random_word = "fancy"
    player_guess = Guess()
    player_guess.word = "fancy"

    result = check_letters(player_guess, word)

    assert result == {0: "green",
                      1: "green",
                      2: "green",
                      3: "green",
                      4: "green"}

def test_check_letters_yellow():
    word = Word()
    word.random_word = "state"
    player_guess = Guess()
    player_guess.word = "taste"

    result = check_letters(player_guess, word)

    assert result == {0: "yellow",
                      1: "yellow",
                      2: "yellow",
                      3: "green",
                      4: "green"}

def test_check_letters_wrong():
    word = Word()
    word.random_word = "ninja"
    player_guess = Guess()
    player_guess.word = "femur"

    result = check_letters(player_guess, word)

    assert result == {0: None,
                      1: None,
                      2: None,
                      3: None,
                      4: None}