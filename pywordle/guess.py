from PyDictionary import PyDictionary

dictionary = PyDictionary()

class Guess():
    def __init__(self, player, guess=None):
        self.player = player
        self.guess = None if guess is None else guess
        self.GREEN_LETTERS = 0
        self.MAX_ATTEMPTS = 6

    def correct_letters(self):
        self.GREEN_LETTERS += 1

    @classmethod
    def get_guess(cls):
        new_guess = input("Guess word: ").lower().strip()
        return Guess(None, new_guess)
    
    def validate(self):
        MAX_LETTERS = 5

        if dictionary.meaning(self.guess, 
                        disable_errors=True) and len(self.guess) == MAX_LETTERS:
            return True
        
        return False
    