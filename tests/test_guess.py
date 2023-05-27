from pywordle.guess import Guess

def test_validate_guess():
    guess = Guess(None)
    guess = guess.validate("fancy")

    assert guess == True

def test_invalid_guess():
    guess = Guess(None)
    guess = guess.validate("aaaaa")

    assert not guess

def test_valid_word_invalid_guess():
    guess = Guess(None)
    guess = guess.validate("banana")

    assert not guess