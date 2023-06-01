import pytest
from pywordle.guess import Guess

def test_constructor_before_guess():
    guess = Guess(None)

    assert guess.GREEN_LETTERS == 0
    assert guess.MAX_ATTEMPTS == 6

def test_constructor_player_made_guess():
    guess = Guess("stove")

    assert guess.word == "stove"

def test_correct_letters():
    guess = Guess(None)
    guess.correct_letters()

    assert guess.GREEN_LETTERS == 1

    guess.correct_letters()

    assert guess.GREEN_LETTERS == 2

def test_validate_guess():
    guess = Guess("fancy")
    is_valid = guess.validate()

    assert is_valid

def test_invalid_guess():
    guess = Guess("aaaaaa")
    is_valid = guess.validate()

    assert not is_valid

def test_valid_word_too_long():
    guess = Guess("banana")
    is_valid = guess.validate()

    assert not is_valid

def test_valid_word_too_short():
    guess = Guess("sad")
    is_valid = guess.validate()

    assert not is_valid