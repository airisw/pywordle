# PyWordle
#### Description
Inspired by the sensational Wordle game published by NYT, this is the same word puzzle game developed in Python using the Wonderwords library to randomly generate words.
#### Rules
Just like in Wordle, the goal is to guess the 5-letter word in 6 trials or less. Upon entering the word, players may see some letters turn green, yellow, or remain the same color.

A green letter means that this letter is correct. A letter in yellow means that the word contains this letter but in another position. And if the letter doesn't change color, this means it's incorrect.

Lastly, all guesses must be real English words.
#### Instructions
Run `pip install -r requirements.txt` to install the necessary libraries (Wonderwords, PyDictionary, termcolor) to run the program.
#### How It Works
We use the Wonderwords package to generate a random word every time we run the program. Because the words in Wordle always have 5 letters, the length is set to be exactly 5 characters.

The player is prompted to enter a 5-letter word. To check if the word is valid in English, we use the PyDictionary library to look up its definition. In case there is no meaning, this means the word is not valid so it returns False instead.

After this, the program will check if the word has been guessed previously. If it is a new guess, it will check the position of each letter and print out the word in green or yellow if the letters are right.

There is also a tracker to count how many remaining attempts there are left at the end of each turn. By the end of the round, the game will display either a congratulations message or a sad one if the player has lost.
#### Unit Tests
There are 3 unit tests included to test out if the functions `validate_guess()`, `check_letters()`, and `get_remaining_attempts()` are working properly.

The function `validate_guess()` is responsible to check if the word guessed is a real English word and if there is 5 characters.

The function `check_letters()` iterates through every letter of the guessed word and compares it to each letter of our random word to find ouf if the positions are correct.

The function `get_remaining_attempts()` keeps track of how many chances the player still has.
#### Future Implementations
Some ideas for future development are:
- Scoreboard: Track how many points the player has so far
- Keyboard display: Display the alphabet in a keyboard layout, like in the original game, for a better visualization of which letters could be important

These plans are subject to change.
#### Acknowledgement
This project was inspired by the game Wordle created by Josh Wardle and published by NYT.
