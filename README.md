# PyWordle

## Description
Inspired by the popular Wordle game published by NYT, this is the same word puzzle game developed in Python using the Wonderwords library to randomly generate words.

This project was redesigned using OOP principles.

## Rules
Just like in Wordle, the goal is to guess the 5-letter word in 6 trials or less. Upon entering the word, players may see some letters turn green, yellow, or red.

A green letter means that this letter is correct. A yellow letter means that the word contains this letter in a different position. A letter in red means that it's incorrect.

Lastly, all guesses must be real English words.

## Instructions
1. Clone the project and navigate to the project directory:
```
git clone https://github.com/airisw/pywordle.git
cd pywordle
```

2. Create a virtual environment for this project:
```
python3 -m venv venv
```

3. Activate the virtual environment:
```
source venv/bin/activate
```

4. Install the necessary dependencies:
```
pip install -r requirements.txt
```

5. Run the program:
```
python -m pywordle.main
```

## How It Works
We use the Wonderwords package to generate a random word every time we run the program. Because the words in Wordle always have 5 letters, the length is set to be exactly 5 characters.

The player is prompted to enter a 5-letter word. To check if the word is valid in English, we use the PyDictionary library to look up its definition. In case there is no meaning, this means the word is not valid, so it returns `False` instead.

The program will check if the word has been guessed previously. If it's a new guess, it will check for the position of each letter, and print out the word in green, yellow, or red according to its position and if the letters are correct.

There is also a tracker to count how many remaining attempts there are left at the end of each turn. By the end of the round, the game will display either a congratulations message or the correct answer in case the player has lost.

## Unit Tests
This project includes a test suite to ensure the correctness of the game logic. The tests are organized into three files.

- `test_guess.py`: This file contains tests related to the guessing functionality of the game and the guess validation.
- `test_main.py`: This file contains tests for the helper function `check_letters`, which is responsible for checking the color for each letter based on the game rules.
- `test_player.py`: This file contains tests related to how many attempts the player has throughout the round.

To run all existing tests in this project:
```
pytest
```

## Future Implementations
Some ideas for future development are:
- Scoreboard: Track how many points the player has so far
- Keyboard display: Display the alphabet in a keyboard layout, like in the original game, for a better visualization of which letters could be important

These plans are subject to change.

## Acknowledgement
This project was inspired by the game Wordle created by Josh Wardle and published by NYT.
