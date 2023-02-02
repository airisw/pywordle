from pywordle import validate_guess, check_letters_color, get_remaining_attempts

def test_validate_guess():
    assert validate_guess("pizza", 5) == True
    assert validate_guess("xyzab", 5) == False
    assert validate_guess("12345", 5) == False
    assert validate_guess("p1zz4", 5) == False

def test_check_letters():
    assert check_letters_color("twine", "stale") == ({1: "yellow", 2: None, 3: None, 4: None, 5: "green"}, 1)
    assert check_letters_color("funny", "stale") == ({1: None, 2: None, 3: None, 4: None, 5: None}, 0)
    assert check_letters_color("sassy", "stale") == ({1: "green", 2: "yellow", 3: "yellow", 4: "yellow", 5: None}, 1)

def test_get_remaining_attempts():
    assert get_remaining_attempts(3, 6) == "You have 3 attempts left"