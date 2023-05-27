import pytest
from pywordle.guess import Guess
from pywordle.player import Player

def test_constructor_before_guess():
    guess = Guess(None)

    assert guess.GREEN_LETTERS == 0
    assert guess.MAX_ATTEMPTS == 6

def test_constructor_player_made_guess():
    new_player = Player()
    guess = Guess(new_player, "stove")

    assert guess.player == new_player
    assert guess.word == "stove"

def test_correct_letters():
    guess = Guess(None)
    guess.correct_letters()

    assert guess.GREEN_LETTERS == 1

def test_validate_guess():
    guess = Guess(None, "fancy")
    is_valid = guess.validate()

    assert is_valid

def test_invalid_guess():
    guess = Guess(None, "aaaaaa")
    is_valid = guess.validate()

    assert not is_valid

def test_valid_word_too_long():
    guess = Guess(None, "banana")
    is_valid = guess.validate()

    assert not is_valid

def test_valid_word_too_short():
    guess = Guess(None, "sad")
    is_valid = guess.validate()

    assert not is_valid